"""Main View classes for the Spanglish app."""
from django.db import IntegrityError
from spanglish.models import Category, Language, Word
from spanglish.serializers import CategorySerializer, LanguageSerializer, WordSerializer
from rest_framework import generics, status, views, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# from fedalapi.permissions import IsOwner
from fedalapi.throttles import SpanglishRateThrottle
from django.conf import settings
from django.core.cache import cache
import logging


CACHE_TTL = getattr(settings, 'CACHE_TTL', 10)
logger = logging.getLogger('spanglish')


class CategoryViews(viewsets.ModelViewSet):
    """uses the ModelViewSet as there is nothing special about
    the views of the category. all standard CRUD operations."""

    throttle_classes = (SpanglishRateThrottle, )
    throttle_scope = 'spanglish'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'

class LanguageViews(viewsets.ModelViewSet):
    """uses the ModelViewSet as there is nothing special about
    the views of the language. all standard CRUD operations."""

    throttle_classes = (SpanglishRateThrottle, )
    throttle_scope = 'spanglish'
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    name = 'language-list'

class WordCreateListView(views.APIView):
    """use for the post, get all requests only."""

    def post(self, request):
        """create a word object and return an http error response for an 
        exception."""

        serializer = WordSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            try:

                serializer.save()
                return Response(status=status.HTTP_201_CREATED)

            except  IntegrityError as e:
                serializer.error_messages = {
                    'INTEGRITY_ERROR': 'INVALID LanguageId or CategoryId'
                }
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

            except Exception as e:
                serializer.error_messages = {
                    'ERROR': str(e)
                }
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
            

    def get(self, request):
        """returns a list of word objects."""

        queryset = Word.objects.all()
        serializer = WordSerializer(queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class WordUpdateDeleteDetails(views.APIView):
    """expects a pk in the request. used for get, put and delete. """

    def get(self, request, pk):
        """get a single word by providing the pk."""
    
        word = Word.objects.get(pk=pk)
        serializer = WordSerializer(word)
        return Response(serializer.data)


    def patch(self, request, pk):
        """update a word object. """

        word = Word.objects.get(pk=pk)
        serializer = WordSerializer(word, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        """delete a word object by providing the pk"""

        word = Word.objects.get(pk=pk)
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class WordViews(viewsets.ModelViewSet):
#     """uses the ModelViewSet as there is nothing special about
#     the views of the word. all standard CRUD operations."""

#     # permissions_classes = (IsAuthenticatedOrReadOnly, )
#     throttle_classes = (SpanglishRateThrottle, )
#     throttle_scope = 'spanglish'
#     queryset = Word.objects.all()
#     serializer_class = WordSerializer
#     name = 'word-list'

# class WordListView(generics.ListAPIView):
#     """Containes the get request only for the Words."""

#     permissions_classes = (IsAuthenticatedOrReadOnly, )
#     throttle_classes = (SpanglishRateThrottle, )
#     throttle_scope = 'spanglish'
#     name = "words-list"
#     queryset = Word.objects.all()

#     def get(self, request, iso1):
#         """Return a list of all words based on the iso1 param."""
#         logger.debug("iso1 param received: %s" % iso1)

#         queryset = Word.words.get_all_words_by_language(iso1=iso1)
#         serializer = WordSerializer(queryset, many=True)
#         data = serializer.data

#         logger.debug("data returned from serializer: %s" % data)

#         return Response(data, status=status.HTTP_200_OK)


# class ApiRoot(generics.GenericAPIView):
#     """Spanglish apis."""

#     name = 'api-root'
#     _ignore_model_permissions = True

#     def get(self, request, *args, **kwargs):
#         """Return all the apis."""
#         return Response(
#             {
#             }
#         )

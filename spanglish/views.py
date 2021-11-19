"""Main View classes for the Spanglish app."""
from django.db import IntegrityError
from spanglish.models import Category, Language, Word, Sentence, Verb, Translation
from spanglish.serializers import CategorySerializer, LanguageSerializer, SentenceSerializer, SentenceDetailsSerializer, WordSerializer, WordDetailsSerializer, VerbSerializer, TranslationSerializer
from rest_framework import status, views, generics
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# from fedalapi.permissions import IsOwner
from fedalapi.throttles import SpanglishRateThrottle
from django.conf import settings
from django.core.cache import cache
import logging


CACHE_TTL = getattr(settings, 'CACHE_TTL', 10)
logger = logging.getLogger('spanglish')


class CategoryCreateListView(views.APIView):
    """use for the post, get all requests only."""

    def post(self, request):
        """create a catgory object and return an http 200 response. 
        If an integrity exception is returned, it will return it with a 
        customer json response."""

        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                message = {'SUCCESS': 'Category created successfully'}
                return Response(data=message, status=status.HTTP_201_CREATED)

            except  IntegrityError as e:
                serializer.error_messages = {
                    'INTEGRITY_ERROR': str(e)
                }
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

            except Exception as e:
                serializer.error_messages = {
                    'ERROR': str(e)
                }
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
            

    def get(self, request):
        """returns a list of category objects."""

        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CategoryUpdateDeleteDetails(views.APIView):
    """expects a pk in the request. Used for get single category, patch and delete. """

    def get(self, request, pk):
        """get a single category by providing the pk."""
    
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        
        return Response(serializer.data)


    def patch(self, request, pk):
        """update a category object. """

        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)

        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data)
            except Exception as e:
                serializer.error_messages = {
                    'ERROR': str(e)
                }
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        """delete a category object by providing the pk"""

        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            message = {'SUCCESS': 'Category has been deleted successfully'}
            return Response(data=message, status=status.HTTP_204_NO_CONTENT)

        except  IntegrityError as e:
            error_messages = {
                'INTEGRITY_ERROR': 'Can not delete category'
            }
            return Response(error_messages, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error_messages = {
                'ERROR': str(e)
            }
            return Response(error_messages, status=status.HTTP_400_BAD_REQUEST)



class LanguageCreateListView(views.APIView):
    """use for the post, get all requests only."""

    def post(self, request):
        """create a language object and return an http 200 response. 
        If an integrity exception is returned, it will return it with a 
        customer json response."""

        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                message = {'SUCCESS': 'Language created successfully'}
                return Response(data=message, status=status.HTTP_201_CREATED)

            except  IntegrityError as e:
                serializer.error_messages = {
                    'INTEGRITY_ERROR': str(e)
                }
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

            except Exception as e:
                serializer.error_messages = {
                    'ERROR': str(e)
                }
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
            

    def get(self, request):
        """returns a list of language objects."""

        queryset = Language.objects.all()
        serializer = LanguageSerializer(queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class LanguageUpdateDeleteDetails(views.APIView):
    """expects a pk in the request. Used for get single language, patch and delete. """

    def get(self, request, pk):
        """get a single language by providing the pk."""
    
        language = Language.objects.get(pk=pk)
        serializer = LanguageSerializer(language)
        
        return Response(serializer.data)


    def patch(self, request, pk):
        """update a language object. """

        language = Language.objects.get(pk=pk)
        serializer = LanguageSerializer(language, data=request.data, partial=True)

        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data)
            except Exception as e:
                serializer.error_messages = {
                    'ERROR': str(e)
                }
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        """delete a language object by providing the pk"""

        try:
            language = Language.objects.get(pk=pk)
            language.delete()
            message = {'SUCCESS': 'Language has been deleted successfully'}
            return Response(data=message, status=status.HTTP_204_NO_CONTENT)

        except  IntegrityError as e:
            error_messages = {
                'INTEGRITY_ERROR': 'Can not delete language'
            }
            return Response(error_messages, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error_messages = {
                'ERROR': str(e)
            }
            return Response(error_messages, status=status.HTTP_400_BAD_REQUEST)



class WordCreateListView(views.APIView):
    """use for the post, get all requests only."""

    
    def post(self, request):
        """create a sentence object and return an http 200 response. 
        If an integrity exception is returned, it will return it with a 
        customer json response."""

        serializer = WordSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)

            except  IntegrityError as e:
                serializer.error_messages = {
                    'INTEGRITY_ERROR': f'{e}'
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
        serializer = WordDetailsSerializer(word)
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


class VerbCreateListView(generics.ListCreateAPIView):
    """use for the post, get all requests only."""

    logger.debug(f"LOGGING")
    def post(self, request):
        """create a verb object and return an http 200 response. 
        If an integrity exception is returned, it will return it with a 
        customer json response."""

        serializer = VerbSerializer(data=request.data)
        
        valid = serializer.is_valid(raise_exception=True)
        logger.info(f"valid received {valid}")
        logger.debug(f"valid errors {serializer.errors}")
        if valid:
            try:
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)

            except  IntegrityError as e:
                serializer.error_messages = {
                    'INTEGRITY_ERROR': f'INVALID Tense or WordId: {e}'
                }
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

            except Exception as e:
                serializer.error_messages = {
                    'ERROR': str(e)
                }
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        else:
            msg = {'ERROR': f'{serializer.errors}'}
            return Response(msg, status=status.HTTP_409_CONFLICT)
            

    def get(self, request):
        """returns a list of verb objects."""

        queryset = Verb.objects.all()
        serializer = VerbSerializer(queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class VerbUpdateDeleteDetails(views.APIView):
    """expects a pk in the request. Used for get single verb, patch and delete. """

    def get(self, request, pk):
        """get a single verb by providing the pk."""
    
        verb = Verb.objects.get(pk=pk)
        serializer = VerbSerializer(verb)
        
        return Response(serializer.data)


    def patch(self, request, pk):
        """update a verb object. """

        verb = Verb.objects.get(pk=pk)
        serializer = VerbSerializer(verb, data=request.data, partial=True)

        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data)
            except Exception as e:
                serializer.error_messages = {
                    'ERROR': str(e)
                }
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        """delete a word object by providing the pk"""

        verb = Verb.objects.get(pk=pk)
        verb.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SentenceCreateListView(views.APIView):
    """use for the post, get all requests only."""

    def post(self, request):
        """create a sentence object and return an http 200 response. 
        If an integrity exception is returned, it will return it with a 
        customer json response."""

        serializer = SentenceSerializer(data=request.data)
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
        """returns a list of sentence objects."""

        queryset = Sentence.objects.all()
        serializer = SentenceSerializer(queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class SentenceUpdateDeleteDetails(views.APIView):
    """expects a pk in the request. Used for get single sentence, patch and delete. """

    def get(self, request, pk):
        """get a single sentence by providing the pk."""
    
        sentence = Sentence.objects.get(pk=pk)
        serializer = SentenceDetailsSerializer(sentence)
        
        return Response(serializer.data)


    def patch(self, request, pk):
        """update a sentence object. """

        sentence = Sentence.objects.get(pk=pk)
        serializer = SentenceSerializer(sentence, data=request.data, partial=True)

        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data)
            except Exception as e:
                serializer.error_messages = {
                    'ERROR': str(e)
                }
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        """delete a sentence object by providing the pk"""

        sentence = Sentence.objects.get(pk=pk)
        sentence.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TranslationCreateListView(views.APIView):
    """use for the post, get all requests only."""

    def post(self, request):
        """create a translation object and return an http 200 response. 
        If an integrity exception is returned, it will return it with a 
        customer json response."""

        serializer = TranslationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)

            except  IntegrityError as e:
                serializer.error_messages = {
                    'INTEGRITY_ERROR': 'INVALID LanguageId'
                }
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

            except Exception as e:
                serializer.error_messages = {
                    'ERROR': str(e)
                }
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
            

    def get(self, request):
        """returns a list of translation objects."""

        queryset = Translation.objects.all()
        serializer = TranslationSerializer(queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class TranslationUpdateDeleteDetails(views.APIView):
    """expects a pk in the request. Used for get single translation, patch and delete. """

    def get(self, request, pk):
        """get a single translation by providing the pk."""
    
        translation = Translation.objects.get(pk=pk)
        serializer = TranslationSerializer(translation)
        
        return Response(serializer.data)


    def patch(self, request, pk):
        """update a translation object. """

        translation = Translation.objects.get(pk=pk)
        serializer = TranslationSerializer(translation, data=request.data, partial=True)

        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data)
            except Exception as e:
                serializer.error_messages = {
                    'ERROR': str(e)
                }
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        """delete a translation object by providing the pk"""

        try:
            translation = Translation.objects.get(pk=pk)
            translation.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            error_messages = {
                'ERROR': str(e)
            }
            return Response(error_messages, status=status.HTTP_400_BAD_REQUEST)



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

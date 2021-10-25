"""Spanglish app views urls."""

from django.urls import path, include
from . import views
from rest_framework import routers

# trailing_slash=False is required with the /? to append a slash if the 
# request doesn't include it. 
router = routers.DefaultRouter(trailing_slash=False)

# router.register(r'category/?', views.CategoryViews)
# router.register(r'language/?', views.LanguageViews)
# router.register(r'word', views.WordCreateUpdateView)

urlpatterns = [
    path('categories/', views.CategoryCreateListView.as_view(), name='category-create-list'),
    path('category/<int:pk>/', views.CategoryUpdateDeleteDetails.as_view(), name='category-details'),
    path('languages/', views.LanguageCreateListView.as_view(), name='language-create-list'),
    path('language/<int:pk>/', views.LanguageUpdateDeleteDetails.as_view(), name='language-details'),
    path('words/', views.WordCreateListView.as_view(), name='word-create-list'),
    path('word/<int:pk>/', views.WordUpdateDeleteDetails.as_view(), name='word-details'),
    path('verbs/', views.VerbCreateListView.as_view(), name='verb-create-list'),
    path('verb/<int:pk>/', views.VerbUpdateDeleteDetails.as_view(), name='verb-details'),
    path('sentences/', views.SentenceCreateListView.as_view(), name='sentence-create-list'),
    path('sentence/<int:pk>/', views.SentenceUpdateDeleteDetails.as_view(), name='sentence-details'),
    path('translations/', views.TranslationCreateListView.as_view(), name='tranlation-create-list'),
    path('translation/<int:pk>/', views.TranslationUpdateDeleteDetails.as_view(), name='translation-details'),    
    path('', include(router.urls)),
    # url(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]

# urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
# urlpatterns += router.urls
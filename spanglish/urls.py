"""Spanglish app views urls."""

from django.urls import path, include
from . import views
from rest_framework import routers

# trailing_slash=False is required with the /? to append a slash if the 
# request doesn't include it. 
router = routers.DefaultRouter(trailing_slash=False)

router.register(r'category/?', views.CategoryViews)
router.register(r'language/?', views.LanguageViews)
# router.register(r'word', views.WordCreateUpdateView)

urlpatterns = [
    # url(r'^category/(?P<name>[a-z]{2})/$',
    #     views.CategoryViews.as_view(), name=views.CategoryViews.name),
    # url(r'^words/language/(?P<iso1>[a-z]{2})/$',
    #     views.WordListView.as_view(), name=views.WordListView.name),
    path('words/', views.WordCreateListView.as_view(), name='word-create-list'),
    path('word/<int:pk>/', views.WordUpdateDeleteDetails.as_view(), name='word-details'),
    path('', include(router.urls)),
    # url(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]

# urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
# urlpatterns += router.urls
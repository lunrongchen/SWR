"""SWR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from wordvector import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
#router = DefaultRouter()
#router.register(r'wordvector', views.WordVectorViewSet)

urlpatterns = patterns('',
    #url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^wordvectors/$', views.WordvectorList.as_view()),
    url(r'^wordvectors/(?P<data_src>\w+)/(?P<dimension>[0-9]+)/(?P<word_text>\w+)/$', views.WordvectorDetail.as_view()),
)
urlpatterns = format_suffix_patterns(urlpatterns);

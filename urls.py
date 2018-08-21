from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list$', views.list, name='list'),
    url(r'^enquete$', views.enquete, name='enquete'),
    url(r'^interception', views.interception, name='interception'),
]

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),  #this goes to localhost:8000/users
    url(r'^/new$', views.click_add_new_user),
    url(r'^/create$', views.create),
    url(r'^/goback$', views.go_back),
    url(r'^/(?P<id>\d+)$', views.show),
    url(r'^/(?P<id>\d+)/edit$', views.edit),
    url(r'^/(?P<id>\d+)/update$', views.update),
    url(r'^/(?P<id>\d+)/destory$', views.destory),
    
]
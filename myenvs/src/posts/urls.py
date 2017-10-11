
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.posts_home),
    url(r'^act/$', views.posts_act),
    url(r'^post/$', views.posts_post),
    url(r'^create/$', views.posts_create),
    url(r'^update/$', views.posts_update),
    # url(r'^detail/$', views.posts_detail),
    # url(r'^detail/(\d+)/$', views.posts_detail),
    # url(r'^detail/(?P<id>\d+)/$', views.posts_detail),
    url(r'^detail/(?P<id>\d+)/$', views.posts_detail,name="detail"),
    url(r'^delete/$', views.posts_delete),
    url(r'^', views.posts_home),
]


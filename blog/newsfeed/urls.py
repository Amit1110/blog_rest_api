from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^post_put/', views.post_put, name='put'),
    url(r'^list/', views.list, name='list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete, name='delete'),
]

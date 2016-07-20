from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^courses/add/?$', views.course_add),
	url(r'^courses/destroy/(?P<id>\d+)$', views.course_destroy),
	url(r'^courses/delete/(?P<id>\d+)$', views.course_delete),
]
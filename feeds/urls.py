from django.contrib import admin
from django.urls import path, include
from feeds import views

urlpatterns = [
    path("", views.show_feed),
	path("<int:feed_id>/<str:feed_content>", views.one_feed),
    path("all/", views.all_feed),
]
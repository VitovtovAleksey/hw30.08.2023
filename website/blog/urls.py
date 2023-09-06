from django.urls import path
from. import views

urlpatterns = [
    path("", views.index),
    path("post", views.post),
    path("blog", views.index),
    path("blog/post", views.post),
    path("blog/about", views.about),
    path("blog/services", views.services),
    path("blog/contact", views.contact),
]

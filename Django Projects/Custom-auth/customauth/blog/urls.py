from django.urls import path

from .views import blog_list, blog_detail, blog_create, blog_edit, blog_delete, my_blogs

urlpatterns = [
    path("", blog_list, name="blog_list"),
    path("my/", my_blogs, name="my_blogs"),
    path("create/", blog_create, name="blog_create"),
    path("<slug:slug>/", blog_detail, name="blog_detail"),
    path("<slug:slug>/edit/", blog_edit, name="blog_edit"),
    path("<slug:slug>/delete/", blog_delete, name="blog_delete"),
]


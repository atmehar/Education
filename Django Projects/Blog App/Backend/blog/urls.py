from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('blogs/', views.blog_list),
    path('blogs/<slug:slug>/', views.blog_detail),

    path('create/', views.create_blog),
    path('edit/<int:id>/', views.edit_blog),
    path('delete/<int:id>/', views.delete_blog),

    path('profile/', views.profile),
]
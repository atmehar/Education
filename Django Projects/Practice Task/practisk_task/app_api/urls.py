from django.urls import path
from .views import user_list_create, user_detail, index

urlpatterns = [
    path('', index, name='index'),
    path('users/', user_list_create),
    path('users/<int:pk>/', user_detail),
]

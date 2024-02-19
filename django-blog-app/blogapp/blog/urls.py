from django.urls import path,include
from . import views

urlpatterns = [
    path('get-post/', views.get_posts),
    path('create-post/',views.create_post),
    path('update-post/<int:pk>',views.update_post),
    path('delete-post/<int:pk>',views.delete_post)
]
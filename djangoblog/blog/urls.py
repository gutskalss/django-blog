from django.urls import path
from .views import Home, AddPost

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add-post/', AddPost.as_view(), name='add_post'),
]

from django.urls import path
from .views import home, video_page, music_page
urlpatterns = [
    path('', home, name='home'),
    path('video/', video_page, name='video'),
    path('audio/', music_page, name='audio'),
]
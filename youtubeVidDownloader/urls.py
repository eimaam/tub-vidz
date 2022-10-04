from django.urls import path
from . import views

urlpatterns = [
    path('', views.ytbVidHome, name='YoutubeHome'),
    path('download/', views.ytbVidDownloader),
]

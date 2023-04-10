from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('speechpage',views.speechpage,name='speechpage'),
    path('translate',views.translate,name='translate'),
    #path('speakspeech',views.speakspeech,name='speakspeech'),
]
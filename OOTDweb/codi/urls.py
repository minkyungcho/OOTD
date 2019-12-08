from django.urls import path
from . import views as codi_views

app_name = 'codi'

urlpatterns = [
    path('', codi_views.index, name="codi"),
    path('home/', codi_views.home, name="home"),
    path('codiWorldcup/', codi_views.codiWorldcup, name="codiWorldcup"),
    path('myCloset/', codi_views.myCloset, name="myCloset"),
    path('weather/',codi_views.getWeather, name="getWeather"),
 ]
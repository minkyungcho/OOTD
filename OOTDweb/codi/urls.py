from django.urls import path
from . import views as codi_views

app_name = 'codi'

urlpatterns = [
    path('', codi_views.index, name="codi"),
    path('home/', codi_views.home, name="home"),
    path('codiWorldcup/', codi_views.codiWorldcup, name="codiWorldcup"),
    path('codiBook/', codi_views.codiBook, name="codiBook"),
    path('myCloset/', codi_views.myCloset, name="myCloset"),
    path('mwCloset/addCloth', codi_views.addCloth, name="addCloth"),
    path('weather/',codi_views.getWeather, name="getWeather"),
 ]
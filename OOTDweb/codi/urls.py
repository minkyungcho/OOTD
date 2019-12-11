from django.urls import path
from . import views as codi_views

app_name = 'codi'

urlpatterns = [
    path('', codi_views.home, name="codi"),
    path('codiWorldcup/', codi_views.codiWorldcup, name="codiWorldcup"),
    path('codiWorldcup/addCodicupResult', codi_views.addCodicupResult, name="addCodicupResult"),
    path('codicupResult/', codi_views.codicupResult, name="codicupResult"),
    path('codiBook/', codi_views.codiBook, name="codiBook"),
    path('myCloset/', codi_views.myCloset, name="myCloset"),
    path('mwCloset/addCloth', codi_views.addCloth, name="addCloth"),
    path('mwCloset/getClothList', codi_views.getClothList, name="getClothList"),
    path('mwCloset/add', codi_views.add, name="add"),
    path('weather/',codi_views.getWeather, name="getWeather"),
    path('mypage/', codi_views.mypage, name="mypage"),
    path('codiBook', codi_views.codiBook, name="codiBook"),
 ]
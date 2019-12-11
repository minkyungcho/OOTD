from django.urls import path
from . import views as codi_views

app_name = 'codi'

urlpatterns = [
    path('', codi_views.home, name="codi"),
    path('codiWorldcup/', codi_views.codiWorldcup, name="codiWorldcup"),
    path('codiBook/', codi_views.codiBook, name="codiBook"),
    path('codiBooks/<int:user_id>/', codi_views.codiBooks, name="codiBooks"),
    path('codiBook/<int:article_id>/delete', codi_views.delete, name="delete"),
    path('allCodiBook/', codi_views.allCodiBook, name="allCodiBook"),
    path('myCloset/', codi_views.myCloset, name="myCloset"),
    path('mwCloset/addCloth', codi_views.addCloth, name="addCloth"),
    path('weather/',codi_views.getWeather, name="getWeather"),
    path('mypage/', codi_views.mypage, name="mypage"),
 ]
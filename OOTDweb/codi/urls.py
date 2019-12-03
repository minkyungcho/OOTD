from django.urls import path
from . import views as codi_views

app_name = 'codi'

urlpatterns = [
    path('', codi_views.index, name="codi"),
    path('home/', codi_views.home, name="home"),
    path('about/', codi_views.about, name="about")
 ]
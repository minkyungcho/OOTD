from django.urls import path
from . import views as codi_views

urlpatterns = [
    path('', codi_views.index, name="codi"),
 ]
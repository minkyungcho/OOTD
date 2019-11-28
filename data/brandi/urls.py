from django.urls import path
from . import views as brandi_views

urlpatterns = [
    path('', brandi_views.index, name="brandies"),
]
    
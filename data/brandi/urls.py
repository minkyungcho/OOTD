from django.urls import path
from . import views as brandi_views

urlpatterns = [
    path('', brandi_views.index, name="index"),
    path('link/<int:category_id>/', brandi_views.link, name="link"),
    path('product/<int:product_id>/', brandi_views.product, name="product"),
    path('product/detail/<int:product_id>/', brandi_views.detail, name="detail"),
]
    
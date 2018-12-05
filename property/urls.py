from django.urls import path
from .views import property_create, property_detail, property_edit

urlpatterns = [
    path('property/create/', property_create, name='property_create'),
    path('property/<int:id>/details/', property_detail, name='property_detail'),
    path('property/<int:id>/edit/', property_edit, name='property_edit'),

]

from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(),name="about"),
    path('create/', ProjectCreateView.as_view(),name="create"),
    # path('edit/<int:pk>', ProjectEditView.as_view(),name="edit"),
    path('delete/<int:pk>', ProjectDeleteView.as_view(),name="delete"),

    path('location/', buildingAddress_input, name='location-views'),
    path('individual/<int:building_id>/',IndividualView, name='individual-views'),
    path('customer/<int:building_id>/',CustomerView, name='resiliance-views')

]
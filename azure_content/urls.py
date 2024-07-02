from django.urls import path
from .views import *

urlpatterns = [
    path('', LandingView, name="landing"),
    path('home/', home_view, name="home"),
    path('about/', AboutView.as_view(),name="about"),
    # path('', ProjectCreateView.as_view(),name="create"),
    path('edit/<int:building_id>', buildingAddress_edit,name="edit"),
    path('details/<int:building_id>', buildingAddress_details,name="details"),

    path('delete/<int:pk>', ProjectDeleteView.as_view(),name="delete"),

    path('create/', buildingAddress_input, name='create-views'),
    path('individual/<int:building_id>/',IndividualView, name='individual-views'),
    path('customer/<int:building_id>/',CustomerView, name='resiliance-views'),
    path('geojson/', geojson_view, name='geojson_view'),
    path('merut_geojson/', merut_geojson_view, name='merut_geojson_view'),
    path('lucknow_geojson/', lucknow_geojson_view, name='lucknow_geojson_view'),
    path('merut_flood_geojson/', merut_flood_geojson_view, name='merut_flood_geojson_view'),
    path('lucknow_flood_geojson/', lucknow_flood_geojson_view, name='lucknow_flood_geojson_view'),

    path('baramullah_geojson/', baramullah_geojson_view, name='baramullah_geojson_view'),
    path('katra_geojson/', katra_geojson_view, name='katra_geojson_view'),

    path('mallofindia_flood_geojson/', mallofindia_flood_geojson_view, name='mallofindia_flood_geojson_view'),
    path('mallofindia_heatwave_geojson/', mallofindi_heatwave_geojson_view, name='mallofindi_heatwave_geojson_view'),
    path('montera_flood_geojson/', montera_flood_geojson_view, name='montera_flood_geojson_view'),
    path('montera_heatwave_geojson/', montera_heatwave_geojson_view, name=' montera_heatwave_geojson_view'),

    path('map/',MapView, name="map-view"),
    path('export/csv/', export_csv, name='export_csv'),
]


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
    # path('geojson/', geojson_view, name='geojson_view'),
    # path('merut_geojson/', merut_geojson_view, name='merut_geojson_view'),
    # path('lucknow_geojson/', lucknow_geojson_view, name='lucknow_geojson_view'),
    # path('merut_flood_geojson/', merut_flood_geojson_view, name='merut_flood_geojson_view'),
    # path('lucknow_flood_geojson/', lucknow_flood_geojson_view, name='lucknow_flood_geojson_view'),

    # path('baramullah_geojson/', baramullah_geojson_view, name='baramullah_geojson_view'),
    # path('katra_geojson/', katra_geojson_view, name='katra_geojson_view'),

    path('mallofindia_flood_geojson/', mallofindia_flood_geojson_view, name='mallofindia_flood_geojson_view'),
    path('mallofindia_heatwave_geojson/', mallofindi_heatwave_geojson_view, name='mallofindi_heatwave_geojson_view'),
    path('montera_flood_geojson/', montera_flood_geojson_view, name='montera_flood_geojson_view'),
    path('montera_heatwave_geojson/', montera_heatwave_geojson_view, name=' montera_heatwave_geojson_view'),

    path('ahemdabad_flood_geojson/', ahemdabad_flood_geojson_view, name='ahemdabad_flood_geojson_view'),
    path('anubhava_flood_geojson/', anubhava_flood_geojson_view, name='anubhava_flood_geojson_view'),
    path('bangalore_flood_geojson/', bangalore_flood_geojson_view, name='bangalore_flood_geojson_view'),
    path('nolumbur_flood_geojson/', nolumbur_flood_geojson_view, name='nolumbur_flood_geojson_view'),
    path('teynampet_flood_geojson/', teynampet_flood_geojson_view, name='teynampet_flood_geojson_view'),
    path('zirkapur_flood_geojson/', zirkapur_flood_geojson_view, name='zirkapur_flood_geojson_view'),


    path('ahemdabad_heatwave_geojson/', ahemdabad_heatwave_geojson_view, name='ahemdabad_heatwave_geojson_view'),
    path('anubhava_heatwave_geojson/', anubhava_heatwave_geojson_view, name='anubhava_heatwave_geojson_view'),
    path('bangalore_heatwave_geojson/', bangalore_heatwave_geojson_view, name='bangalore_heatwave_geojson_view'),
    path('nolumbur_heatwave_geojson/', nolumbur_heatwave_geojson_view, name='nolumbur_heatwave_geojson_view'),
    path('teynampet_heatwave_geojson/', teynampet_heatwave_geojson_view, name='teynampet_heatwave_geojson_view'),
    path('zirkapur_heatwave_geojson/', zirkapur_heatwave_geojson_view, name='zirkapur_heatwave_geojson_view'),

    path('mumbai_geojson/', mumbai_geojson_view, name='mumbai_geojson_view'),
    path('hyd_final_heatwave_geojson/', hydrabad_heatwave_geojson_view, name='hydrabad_heatwave_geojson_view'),
    path('hyd_final_flood_geojson/', hydrabad_flood_geojson_view, name='hydrabad_flood_geojson_view'),


    path('map/',MapView, name="map-view"),
    path('export/csv/', export_csv, name='export_csv'),
]


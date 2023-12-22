from django.urls import include, path
from . import views
from . import api

urlpatterns = [
    path('', views.Index, name='index'),
    path('api/satellites', api.SatellitesList.as_view(), name='satellites_list_api'),
    path('api/operators', api.OperatorsList.as_view(), name='operators_list_api'),
    path('api/satellite/<int:pk>', api.SatelliteDetails.as_view(), name='satellite_details_api'),
    path('api/operator/<int:pk>', api.OperatorDetails.as_view(), name='operator_details_api'),
    path('api/satellite/add', api.SatelliteAdd.as_view(), name='satellite_add_api'),
    path('api/satellites/query', api.SatellitesQuery.as_view(), name='satellites_query_api'),
]
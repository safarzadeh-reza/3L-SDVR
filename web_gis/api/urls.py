# from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, re_path
from api import views

# urlpatterns = patterns('api.views',
#     #  ex valid call from to  /api/directions/1587848.414,5879564.080,2&1588005.547,5879736.039,2
#     url(r'^directions/(?P<start_coord>[-]?\d+\.?\d+,\d+\.\d+),(?P<start_floor>\d+)&(?P<end_coord>[-]?\d+\.?\d+,\d+\.\d+),(?P<end_floor>\d+)&(?P<route_type>[0-9])/$', 'create_route', name='directions'),
#     url(r'^directions/(?P<start_room_num>\d{5})&(?P<end_room_num>\d{5})&(?P<route_type>[0-9])/$', 'route_room_to_room', name='route-room-to-room'),
#     url(r'^directions/(?P<room_num>\d{5})/$', 'get_room_centroid_node', name='room-center'),
#     url(r'^rooms/$', 'room_list', name='room-list'),

# )
urlpatterns = [
    #     #  ex valid call from to  /api/directions/1587848.414,5879564.080,2&1588005.547,5879736.039,2
    # path('directions/(?P<start_coord>[-]?\d+\.?\d+,\d+\.\d+),(?P<start_floor>\d+)&(?P<end_coord>[-]?\d+\.?\d+,\d+\.\d+),(?P<end_floor>\d+)&(?P<route_type>[0-9])/$', views.create_route, name='directions'),
    # re_path(r'^directions/(?P<start_coord>[-]?\d+\.?\d+,\d+\.\d+),(?P<start_floor>\d+)&(?P<end_coord>[-]?\d+\.?\d+,\d+\.\d+),(?P<end_floor>\d+)&(?P<route_type>[0-9])/$', views.create_route),
    re_path(r'^directions/(?P<start_coord>[-]?\d+\.?\d+,\d+\.\d+)&(?P<end_coord>[-]?\d+\.?\d+,\d+\.\d+)/$', views.direction_result),
    re_path(r'^routes/$', views.rout_finding, name='rout_finding'),

    #     url(r'^directions/(?P<start_room_num>\d{5})&(?P<end_room_num>\d{5})&(?P<route_type>[0-9])/$', 'route_room_to_room', name='route-room-to-room'),
#     url(r'^directions/(?P<room_num>\d{5})/$', 'get_room_centroid_node', name='room-center'),
    re_path(r'^rooms/$', views.room_list, name='room-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path
from .views import landing, new_address, frame_houses,tiny_house, contact, our_wood, natural_edge_banding,our_mission, sliced_veneer

urlpatterns = [
    path('about/', landing, name='landing'),
    path('new_address/', new_address, name='new_address'),
    path('frame-houses/', frame_houses, name='frame_house'),
    path('tiny-house/', tiny_house, name='tiny_house'),
    path('contact/', contact, name='contact'),
    path('our-wood/', our_wood, name='our_wood'),
    path('natural_edge_banding/', natural_edge_banding, name='natural_edge_banding'),
    path('our_mission/', our_mission, name='our_mission'),
    path('sliced_veneer/', sliced_veneer, name='sliced_veneer'),
    
]



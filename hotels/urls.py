from django.urls import path
from . import views

urlpatterns = [
    # URLs para Hotel
    path('hotels', views.HotelListView.as_view(), name='hotel-list'),
    path('hotels/<int:pk>', views.HotelDetailView.as_view(), name='hotel-detail'),

    path('hotels/<int:hotel_id>/rooms', views.HotelRoomListView.as_view(), name='hotel-room-list'),
    path('hotels/<int:hotel_id>/services', views.HotelServiceListView.as_view(), name='hotel-service-list'),
    path('hotels/<int:hotel_id>/images', views.HotelImageListView.as_view(), name='hotel-image-list'),

    # URLs para Room
    path('rooms', views.RoomListView.as_view(), name='room-list'),
    path('rooms/<int:pk>', views.RoomDetailView.as_view(), name='room-detail'),
    path('rooms/<int:room_id>/images', views.RoomImageListView.as_view(), name='room-image-list'),
    # URLs para Service
    path('services', views.ServiceListView.as_view(), name='service-list'),
    path('services/<int:pk>', views.ServiceDetailView.as_view(), name='service-detail'),

    # URLs para HotelImage
    path('hotel-images', views.HotelImageListView.as_view(), name='hotel-image-list'),
    path('hotel-images/<int:pk>', views.HotelImageDetailView.as_view(), name='hotel-image-detail'),

    # URLs para RoomImage
    path('room-images', views.RoomImageListView.as_view(), name='room-image-list'),
    path('room-images/<int:pk>', views.RoomImageDetailView.as_view(), name='room-image-detail'),
]


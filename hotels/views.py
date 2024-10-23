from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Hotel, Room, Service, HotelImage, RoomImage
from .serializers import HotelSerializer, RoomSerializer, ServiceSerializer, HotelImageSerializer, RoomImageSerializer
from .filters import RoomFilter

class HotelListView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['city', 'country', 'stars']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'stars']

class HotelDetailView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = RoomFilter
    search_fields = ['name']
    ordering_fields = ['price', 'floor', 'number']

class RoomDetailView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['hotel', 'is_available']
    search_fields = ['name', 'detail']
    ordering_fields = ['name', 'price']

class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class HotelImageListView(generics.ListAPIView):
    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hotel']

class HotelImageDetailView(generics.RetrieveAPIView):
    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializer

class RoomImageListView(generics.ListAPIView):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['room']

class RoomImageDetailView(generics.RetrieveAPIView):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerializer


class HotelRoomListView(generics.ListAPIView):
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = RoomFilter
    search_fields = ['name']
    ordering_fields = ['price', 'floor', 'number']

    def get_queryset(self):
        hotel_id = self.kwargs['hotel_id']
        return Room.objects.filter(hotel_id=hotel_id)

class HotelServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        hotel_id = self.kwargs['hotel_id']
        return Service.objects.filter(hotel_id=hotel_id)

class HotelImageListView(generics.ListAPIView):
    serializer_class = HotelImageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hotel']

    def get_queryset(self):
        hotel_id = self.kwargs['hotel_id']
        return HotelImage.objects.filter(hotel_id=hotel_id)


class RoomImageListView(generics.ListAPIView):
    serializer_class = RoomImageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['room']

    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return RoomImage.objects.filter(room_id=room_id)


from rest_framework import serializers
from .models import Hotel, Room, Service, HotelImage, RoomImage

class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['id', 'image', 'hotel']

class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['id', 'image', 'room']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'detail', 'price', 'is_available', 'hotel']

class RoomSerializer(serializers.ModelSerializer):
    images = RoomImageSerializer(many=True, read_only=True)
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())
    is_available = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ['id', 'hotel', 'floor', 'number', 'name', 'price', 'state', 'images', 'is_available']

    def get_is_available(self, obj):
        start_date = self.context['request'].query_params.get('start_date')
        end_date = self.context['request'].query_params.get('end_date')
        if start_date and end_date:
            return obj.is_available(start_date, end_date)
        return None

class HotelSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)
    images = serializers.SerializerMethodField()
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'address', 'city', 'country', 'phone', 'email', 'stars', 'description', 'latitude', 'longitude', 'rooms', 'images', 'services']

    def get_images(self, obj):
        return HotelImageSerializer(HotelImage.objects.filter(hotel=obj), many=True).data

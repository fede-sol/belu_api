from django.contrib import admin
from .models import Hotel, Room, Service, HotelImage, RoomImage

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Service)
admin.site.register(HotelImage)
admin.site.register(RoomImage)


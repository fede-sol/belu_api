from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    stars = models.IntegerField()
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotel_images')

class Room(models.Model):
    ROOM_STATE_CHOICES = [
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('maintenance', 'Maintenance'),
    ]

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    floor = models.IntegerField()
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.FloatField()
    state = models.CharField(max_length=255, choices=ROOM_STATE_CHOICES, default='available')

class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_images')

class Service(models.Model):
    name = models.CharField(max_length=255)
    detail = models.TextField()
    price = models.FloatField()
    is_available = models.BooleanField(default=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

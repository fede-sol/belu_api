from django.db import models

class Reservation(models.Model):
    room = models.ForeignKey('hotels.Room', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    user_profile = models.ForeignKey('belu_auth.BeluUserProfile', on_delete=models.CASCADE)
    services = models.ManyToManyField('hotels.Service', blank=True)

class Payment(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_paid = models.DateTimeField(null=True, blank=True)
    last_four_digits = models.CharField(max_length=4)
    payment_method = models.CharField(max_length=255)
    amount = models.FloatField()

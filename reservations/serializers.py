from rest_framework import serializers
from .models import Reservation, Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'amount', 'date_created', 'date_paid', 'last_four_digits', 'payment_method']

class ReservationSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = Reservation
        fields = ['id', 'user_profile', 'room', 'start_date', 'end_date', 'services', 'payment']

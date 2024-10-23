from rest_framework import serializers
from .models import Reservation, Payment
from django.db.models import Q
from django.utils import timezone

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'amount', 'date_created', 'date_paid', 'last_four_digits', 'payment_method']

class ReservationSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = Reservation
        fields = ['id', 'user_profile', 'room', 'start_date', 'end_date', 'services', 'payment']

    def validate(self, data):
        room = data.get('room')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        # Validación de fechas
        if start_date and end_date:
            if end_date <= start_date:
                raise serializers.ValidationError("The end date must be after the start date.")

            if start_date < timezone.now().date():
                raise serializers.ValidationError("The start date cannot be in the past.")

        # Validación de disponibilidad de habitación
        if room and start_date and end_date:
            overlapping_reservations = Reservation.objects.filter(
                Q(room=room) &
                (Q(start_date__lte=start_date, end_date__gte=start_date) |
                 Q(start_date__lte=end_date, end_date__gte=end_date) |
                 Q(start_date__gte=start_date, end_date__lte=end_date))
            ).exclude(id=self.instance.id if self.instance else None)

            if overlapping_reservations.exists():
                raise serializers.ValidationError("The room is not available for the selected dates.")

        return data

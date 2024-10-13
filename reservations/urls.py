from django.urls import path
from . import views

urlpatterns = [
    path('reservations', views.UserReservationListCreateView.as_view(), name='user-reservation-list-create'),
    path('reservations/<int:pk>', views.ReservationDetailView.as_view(), name='reservation-detail'),
]


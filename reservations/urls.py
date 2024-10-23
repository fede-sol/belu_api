from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserReservationListCreateView.as_view(), name='user-reservation-list-create'),
    path('<int:pk>', views.ReservationDetailView.as_view(), name='reservation-detail'),
    path('payments', views.PaymentListView.as_view(), name='payment-list'),
    path('<int:pk>/payments', views.PaymentListByReservationView.as_view(), name='payment-list-by-reservation'),
]


import django_filters
from .models import Room

class RoomFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(method='filter_availability')
    end_date = django_filters.DateFilter(method='filter_availability')

    class Meta:
        model = Room
        fields = ['hotel', 'floor', 'state', 'start_date', 'end_date']

    def filter_availability(self, queryset, name, value):
        start_date = self.data.get('start_date')
        end_date = self.data.get('end_date')

        if start_date and end_date:
            return queryset.filter(
                id__in=[room.id for room in queryset if room.is_available(start_date, end_date)]
            )
        return queryset


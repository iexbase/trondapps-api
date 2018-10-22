from django_filters import FilterSet

from app.models import Item


class ItemFilter(FilterSet):
    class Meta:
        model = Item
        fields = ['name']
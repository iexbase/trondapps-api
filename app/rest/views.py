from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from app.models import Item, ItemStatus, ItemCategory
from app.rest.serializers import ItemsSerializer, StatisticSerializer, ItemStatusSerializer, ItemCategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().filter(is_active=1)
    lookup_field = 'slug'
    serializer_class = ItemsSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', )
    allowed_methods = ('GET', 'POST',)


class StatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ItemStatus.objects.all()
    pagination_class = None
    serializer_class = ItemStatusSerializer
    allow_methods = ('GET',)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ItemCategory.objects.all()
    pagination_class = None
    serializer_class = ItemCategorySerializer
    allow_methods = ('GET',)


class StatisticViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all().filter(is_active=1)
    pagination_class = None
    serializer_class = StatisticSerializer
    allow_methods = ('GET',)

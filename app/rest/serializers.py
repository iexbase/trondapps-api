from abc import ABC

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from rest_framework.filters import SearchFilter

from app.models import Item, ItemStatus
from rest_framework import serializers

from django.core.files.base import ContentFile
import base64
import uuid


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            # base64 encoded image - decode
            format, imgstr = data.split(';base64,')  # format ~= data:image/X,
            ext = format.split('/')[-1]  # guess file extension
            id = uuid.uuid4()
            data = ContentFile(base64.b64decode(imgstr), name=id.urn[9:] + '.' + ext)
        return super(Base64ImageField, self).to_internal_value(data)


class ItemStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemStatus
        fields = ('id', 'name',)


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemStatus
        fields = ('id', 'name',)


class ItemsSerializer(serializers.ModelSerializer):
    lookup_field = 'slug'
    logo_url = Base64ImageField()

    class Meta:
        model = Item
        fields = (
            'slug',
            'name',
            'author',
            'email',
            'short_text',
            'text',
            'website_url',
            'contact_address',
            'software_license',
            'status',
            'category',
            'github',
            'logo_url',
            'launch_url',
            'created_at',
            'updated_at'
        )
        read_only_fields = ('slug',)


class StatisticSerializer(serializers.ModelSerializer):
    project_count = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ('project_count',)

    @staticmethod
    def get_project_count(obj):
        return Item.objects.filter(is_active=1).count()

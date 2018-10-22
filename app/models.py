import re

import unidecode
from django.db import models


# Статус проекта
from django.utils.text import slugify


class ItemStatus(models.Model):
    name = models.CharField(verbose_name="Статус", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


# Категория в которую войдет проект
class ItemCategory(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Список проектов
class Item(models.Model):
    slug = models.SlugField(unique=True, allow_unicode=True, default=None)
    name = models.CharField(max_length=30, unique=True, help_text="The DApp name")
    author = models.CharField(max_length=150, help_text="The DApp author")
    email = models.EmailField(max_length=150, help_text="Email of the primary contact (this will not be made public）")
    short_text = models.CharField(max_length=200, help_text="A short teaser that is simple and descriptive")
    text = models.TextField(help_text="The full description of your event")
    website_url = models.URLField(help_text="A URL to this DApp's website")
    contact_address = models.CharField(max_length=200, blank=True, help_text="TRON account address")
    software_license = models.CharField(max_length=50, blank=True, help_text="(e.g. MIT, GPL)")
    status = models.ForeignKey(ItemStatus, default=1, on_delete=models.CASCADE)
    category = models.ForeignKey(ItemCategory, default=1, on_delete=models.CASCADE)
    github = models.CharField(max_length=200, blank=True, help_text="Social Media Link")
    launch_url = models.URLField(help_text="A URL that will launch this ÐApp directly")
    logo_url = models.ImageField(max_length=100)
    is_active = models.BooleanField(verbose_name="Enabled", default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(re.sub(r'\s+', '-', unidecode.unidecode(self.name).lower().strip()))
        super(Item, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

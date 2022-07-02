from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from .models import BrandPlans


# Register your models here.
admin.site.register(BrandPlans)
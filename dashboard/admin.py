from django.contrib import admin

from dashboard.models import Notes
from . models import *

# Register your models here.
admin.site.register(Notes)
admin.site.register(Homework)
admin.site.register(Todo)
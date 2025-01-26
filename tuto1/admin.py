from django.contrib import admin
from .models import TodoEntry
# Register your models here.

admin.register(TodoEntry)(admin.ModelAdmin)
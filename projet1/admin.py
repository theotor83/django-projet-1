from django.contrib import admin
from .models import TodoEntry, Token
# Register your models here.

admin.site.register(TodoEntry)
admin.site.register(Token)
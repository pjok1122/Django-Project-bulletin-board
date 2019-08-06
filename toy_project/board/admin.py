from django.contrib import admin
from .models import Board
# Register your models here.

class boardAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Board, boardAdmin)
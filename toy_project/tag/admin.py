from django.contrib import admin
from .models import Tag

# Register your models here.
class tagAdmin(admin.ModelAdmin):
    list_display =('name',)

admin.site.register(Tag, tagAdmin)

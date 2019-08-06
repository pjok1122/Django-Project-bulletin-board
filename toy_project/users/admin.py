from django.contrib import admin
from .models import Users
# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display =('username', 'useremail')

admin.site.register(Users, userAdmin)

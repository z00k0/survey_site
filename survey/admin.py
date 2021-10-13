from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import RoomFilling, User, Personal, Visual

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Personal)
admin.site.register(Visual)
admin.site.register(RoomFilling)
# admin.site.register(Beauties)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Personal

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Personal)
# admin.site.register(Equips)
# admin.site.register(ProjectStyles)
# admin.site.register(Beauties)

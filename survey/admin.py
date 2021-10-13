from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Personal, Visual

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Personal)
admin.site.register(Visual)
# admin.site.register(MaterialChoice)
# admin.site.register(Beauties)

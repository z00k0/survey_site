from django.urls import path
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('personal', views.personal, name='personal'),
    path('visual', views.visual, name='visual'),
    path('filling', views.filling, name='filling'),
    path('light', views.light, name='light'),

]
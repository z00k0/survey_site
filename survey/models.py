from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    pass


class Personal(models.Model):
    def user_media_path(instance, filename):
        return f'upload/user_{instance.user.pk:03d}/plan/{filename}'
    user = models.OneToOneField(User, on_delete=CASCADE)
    name = models.CharField(max_length=50, blank=True, default=None)
    survey_date = models.DateTimeField(blank=True, default=None, null=True)
    addr = models.CharField(max_length=200, blank=True, default=None, null=True)
    square = models.FloatField(default=0, blank=True, null=True)
    plan = models.FileField(upload_to=user_media_path, blank=True, null=True)
    composition = models.CharField(max_length=500, blank=True, null=True, default=None)
    interests = models.CharField(max_length=500, blank=True, null=True, default=None)
    budget = models.FloatField(default=0, blank=True, null=True)
    
    class Equips(models.TextChoices):
        v1 = 'v1', _('Хотим все чистовые материалы и оборудование закупать самостоятельно (все вопросы по доставке, приемке, обменам и возвратам остаются на стороне заказчика)'),
        v2 = 'v2', _('Хотим делегировать комплектацию "Профмастероф" (все вопросы по доставке, приемке, обменам и возвратам берет на себя компания)'),
        v3 = 'v3', _('Хотим что-то определенное закупить сами, остальное делегируем "Профмастероф"'),
        v4 = 'v4', _('Другое:')
        # __empty__ = _('(Unknown)')
    
    equip_s = models.CharField(max_length=2, default=None, blank=True, null=True, choices=Equips.choices)
    equip = models.CharField(max_length=500, blank=True, null=True, default=None)

    class ProjectStyles(models.TextChoices):
        v1 = 'v1', _('Мне нужен дизайнер, который разработает проект с моим минимальным участием'),
        v2 = 'v2', _('Я доверяю профессиональному мнению и вкусу дизайнера, просто хочу, чтобы учли пожелания из этой анкеты'),
        v3 = 'v3', _('У меня очень много идей, но не знаю, как их правильно вписать в интерьер. Мне нужны советы и помощь дизайнера, чтобы оформить грамотный интерьер'),
        v4 = 'v4', _('Я четко знаю, чего хочу. Дизайнер нужен только для того, чтобы оформить мои идеи в дизайн-проект')

    project_style = models.CharField(max_length=2, default=None, blank=True, null=True, choices=ProjectStyles.choices)

    class Beauties(models.TextChoices):
        v1 = 'v1', _('Главное, чтобы красиво!'),
        v2 = 'v2', _('Я могу пожертвовать некоторым комфортом ради красивого интерьера'),
        v3 = 'v3', _('Я хочу найти баланс между красотой и практичностью'),
        v4 = 'v4', _('Мне нужен практичный интерьер, даже в ущерб красоте'),
        v5 = 'v5', _('Чем практичнее, тем красивее')

    beauty = models.CharField(max_length=2, default=None, blank=True, null=True, choices=Beauties.choices)


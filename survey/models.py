from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _

from multiselectfield import MultiSelectField

# Create your models here.
class User(AbstractUser):
    pass


class Personal(models.Model):
    def user_media_path(instance, filename):
        return f'upload/user_{instance.user.pk:03d}/plan/{filename}'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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


MATS_CHOICES = (
    ('wood', 'Дерево'),
    ('stone', 'Камень'),
    ('concrete', 'Бетон'),
    ('textile', 'Текстиль'),
    ('leather', 'Кожа'),
    ('glass', 'Стекло'),
    ('metal', 'Металл'),
    ('aged', 'Состаренные поверхности'),
    ('smooth', 'Гладкие поверхности'),
    ('brick', 'Кирпич'),
    ('wallpaper', 'Декоративные обои'),
    ('rails', 'Рейки'),
    ('moldings', 'Молдинги на стенах'),
    ('paintings', 'Картины'),
    ('fresco', 'Фреска/фотообои во всю стену'),
    ('other', 'Другое'),
)

STYLE_CHOICES = (
    ('v01', 'v01'),
    ('v02', 'v02'),
    ('v03', 'v03'),
    ('v04', 'v04'),
    ('v05', 'v05'),
    ('v06', 'v06'),
    ('v07', 'v07'),
    ('v08', 'v08'),
    ('v09', 'v09'),
    ('v10', 'v10'),
    ('v11', 'v11'),
    ('v12', 'v12'),
    ('v13', 'v13'),
    ('v14', 'v14'),
    ('v15', 'v15'),
    ('v16', 'v16'),
    ('v17', 'Другое'),
)

FURNITURE_CHOICES = (
    ('v01', 'ИКЕА'),
    ('v02', 'Любая подходящая готовая мебель'),
    ('v03', 'Встроенная, под заказ'),
    ('v04', 'Другое:'),
)

PLANNING_CHOICES = (
    ('v01', 'Коридор'),
    ('v02', 'Ванная'),
    ('v03', 'Санузел'),
    ('v04', 'Гардеробная'),
    ('v05', 'Спальня'),
    ('v06', 'Кухня'),
    ('v07', 'Кухня-гостиная'),
    ('v08', 'Гостиная'),
    ('v09', 'Детская'),
    ('v10', 'Кабинет'),
    ('v11', 'Балкон'),
    ('v12', 'Лоджия'),
    ('v13', 'Кладовая'),
    ('v14', 'Постирочная'),
    ('v15', 'Гостевая спальня'),
    ('v16', 'Хозблок'),
    ('v17', 'Другое'),
)

PLANNING_TYPE_CHOICES = (
    ('v01', 'Незначительные изменения'),
    ('v02', 'Полная перепланировка'),
    ('v03', 'На усмотрение дизайнера (любая перепланировка это дополнительные затраты на работы)'),
    ('v04', 'Перепланировки не будет'),
)

class Visual(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    materials = MultiSelectField(choices=MATS_CHOICES, default=False) #  , choices=MatChoice.choices
    material_other = models.CharField(max_length=200, null=True, default=None, blank=True)
    styles = MultiSelectField(choices=STYLE_CHOICES, default=False)
    style_other = CharField(max_length=200, null=True, default=None, blank=True)
    unsuitable = CharField(max_length=200, null=True, default=None, blank=True)
    furniture = MultiSelectField(choices=FURNITURE_CHOICES, default=None)
    furniture_other = CharField(max_length=200, null=True, default=None, blank=True)
    planning = MultiSelectField(choices=PLANNING_CHOICES, default=None)
    planning_other = CharField(max_length=200, null=True, default=None, blank=True)
    planning_type = MultiSelectField(choices=PLANNING_TYPE_CHOICES, default=None)
    planning_type_other = CharField(max_length=200, null=True, default=None, blank=True)


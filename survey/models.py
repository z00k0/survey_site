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
    materials = MultiSelectField(choices=MATS_CHOICES, default=None) #  , choices=MatChoice.choices
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

KITCHEN_CHOICES = (
    ('v01', 'Холодильник встроенный'),
    ('v02', 'Холодильник отдельностоящий'),
    ('v03', 'Холодильник отдельностоящий широкий side-by-side'),
    ('v04', 'Посудомоечная машина шириной 60 см (оптимально для семьи из 4 и более человек)'),
    ('v05', 'Посудомоечная машина шириной 45 см (оптимально для семьи до 3 человек)'),
    ('v06', 'Духовка под варочной панелью'),
    ('v07', 'Духовка+Микроволновка в колонне'),
    ('v08', 'Микроволновка отдельностоящая'),
    ('v09', 'Варочная панель на 4 конфорки'),
    ('v10', 'Варочная панель на 2 конфорки'),
    ('v11', 'Диспоузер (измельчитель отходов)'),
    ('v12', 'Стиральная машина'),
    ('v13', 'Фильтр для воды под раковиной'),
    ('v14', 'Раковина одинарная без крыла'),
    ('v15', 'Раковина одинарная с крылом'),
    ('v16', 'Вытяжка отдельная'),
    ('v17', 'Вытяжка встроенная'),
    ('v18', 'Раковина двойная'),
    ('v19', 'Стол на 2 человека'),
    ('v20', 'Стол на 4 человека'),
    ('v21', 'Стол на 6 человек'),
    ('v22', 'Стол должен быть раздвижной'),
    ('v23', 'Круглая форма стола предпочтительнее'),
    ('v24', 'Квадратная/прямоугольная форма стола предпочтительнее'),
    ('v25', 'Телевизор'),
    ('v26', 'Барная стойка'),
    ('v27', 'Предусмотреть много места для хранения'),
    ('v28', 'Предпочтительнее кухня без верхних шкафов'),
    ('v29', 'Другое:'),
)

BEDROOM_CHOICES = (
    ('v01', 'Кровать шириной 160 см'),
    ('v02', 'Кровать шириной 180 см'),
    ('v03', 'Кровать шириной 200 см'),
    ('v04', 'Гардероб'),
    ('v05', 'Комод'),
    ('v06', 'Тумбы прикроватные'),
    ('v07', 'Кресло'),
    ('v08', 'Туалетный столик'),
    ('v09', 'Рабочее место'),
    ('v10', 'Детская кроватка'),
    ('v11', 'Телевизор'),
    ('v12', 'Другое:'),
)

LIVINGROOM_CHOICES = (
    ('v01', 'Диван угловой'),
    ('v02', 'Диван прямой'),
    ('v03', 'ТВ'),
    ('v04', 'Тумба под ТВ'),
    ('v05', 'Система хранения'),
    ('v06', 'Рабочее место'),
    ('v07', 'Другое:'),
)

CHILDROOM_CHOICES = (
    ('v01', 'Кроватка для младенца 60*120'),
    ('v02', 'Кровать детская 80*160'),
    ('v03', 'Кровать полноценная односпальная 90*200'),
    ('v04', 'Кровать полноценная полутороспальная 120*200'),
    ('v05', 'Кровать "растущая"'),
    ('v06', 'Дополнительное спальное место (друзья, родственники)'),
    ('v07', 'Кровать-чердак'),
    ('v08', 'Рабочее место'),
    ('v09', 'Хранение одежды'),
    ('v10', 'Хранение игрушек'),
    ('v11', 'Игровая зона'),
    ('v12', 'Шведская стенка'),
    ('v13', 'Телевизор'),
    ('v14', 'Другое'),
)

BATHROOM_CHOICES = (
    ('v01', 'Ванна чем больше, тем лучше'),
    ('v02', 'Ванна, какая поместится'),
    ('v03', 'Смеситель для ванны+душевой комплект'),
    ('v04', 'Тропический душ'),
    ('v05', 'Душевая'),
    ('v06', 'Унитаз подвесной'),
    ('v07', 'Унитаз с бачком'),
    ('v08', 'Гигиенический душ'),
    ('v09', 'Тумба с раковиной'),
    ('v10', 'Зеркало с подсветкой'),
    ('v11', 'Зеркальный шкафчик'),
    ('v12', 'Стиральная машина'),
    ('v13', 'Сушильная машина'),
    ('v14', 'Полотенцесушитель электрический'),
    ('v15', 'Полотенцесушитель водяной'),
    ('v16', 'Водонагреватель 50 л (оптимально для семьи до 3 человек)'),
    ('v17', 'Водонагреватель 80 л (оптимально для семьи из 4-5 человек)'),
    ('v18', 'Проточный водонагреватель'),
    ('v19', 'Другое'),
)

TOILET_CHOICES = (
    ('v01', 'Душевая'),
    ('v02', 'Унитаз подвесной'),
    ('v03', 'Унитаз с бачком'),
    ('v04', 'Гигиенический душ'),
    ('v05', 'Тумба с раковиной'),
    ('v06', 'Зеркало с подсветкой'),
    ('v07', 'Зеркальный шкафчик'),
    ('v08', 'Стиральная машина'),
    ('v09', 'Сушильная машина'),
    ('v10', 'Полотенцесушитель электрический'),
    ('v11', 'Полотенцесушитель водяной'),
    ('v12', 'Водонагреватель 50 л (оптимально для семьи до 3 человек)'),
    ('v13', 'Водонагреватель 80 л (оптимально для семьи из 4-5 человек)'),
    ('v14', 'Проточный водонагреватель'),
    ('v15', 'Другое'),
)

class RoomFilling(models.Model):
    def user_kitchen_path(instance, filename):
        return f'upload/user_{instance.user.pk:03d}/kitchen_{filename}'
    def user_bedroom_path(instance, filename):
        return f'upload/user_{instance.user.pk:03d}/bedroom_{filename}'
    def user_livingroom_path(instance, filename):
        return f'upload/user_{instance.user.pk:03d}/livingroom_{filename}'
    def user_childroom_path(instance, filename):
        return f'upload/user_{instance.user.pk:03d}/childroom_{filename}'
    def user_bathroom_path(instance, filename):
        return f'upload/user_{instance.user.pk:03d}/bathroom_{filename}'
    def user_toilet_path(instance, filename):
        return f'upload/user_{instance.user.pk:03d}/toilet_{filename}'
    def user_interior_path(instance, filename):
        return f'upload/user_{instance.user.pk:03d}/interior_{filename}'
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kitchen = MultiSelectField(choices=KITCHEN_CHOICES, default=None, null=True, blank=True)
    kitchen_other = models.CharField(max_length=200, null=True, default=None, blank=True)
    kitchen_photo = models.FileField(upload_to=user_kitchen_path, blank=True, null=True)
    bedroom = MultiSelectField(choices=BEDROOM_CHOICES, default=None, null=True, blank=True)
    bedroom_other = models.CharField(max_length=200, null=True, default=None, blank=True)
    bedroom_photo = models.FileField(upload_to=user_bedroom_path, blank=True, null=True)
    livingroom = MultiSelectField(choices=LIVINGROOM_CHOICES, default=None, null=True, blank=True)
    livingroom_other = models.CharField(max_length=200, null=True, default=None, blank=True)
    livingroom_photo = models.FileField(upload_to=user_livingroom_path, blank=True, null=True)
    childroom = MultiSelectField(choices=CHILDROOM_CHOICES, default=None, null=True, blank=True)
    childroom_other = models.CharField(max_length=200, null=True, default=None, blank=True)
    childroom_photo = models.FileField(upload_to=user_childroom_path, blank=True, null=True)
    bathroom = MultiSelectField(choices=BATHROOM_CHOICES, default=None, null=True, blank=True)
    bathroom_other = models.CharField(max_length=200, null=True, default=None, blank=True)
    bathroom_photo = models.FileField(upload_to=user_bathroom_path, blank=True, null=True)
    toilet = MultiSelectField(choices=TOILET_CHOICES, default=None, null=True, blank=True)
    toilet_other = models.CharField(max_length=200, null=True, default=None, blank=True)
    toilet_photo = models.FileField(upload_to=user_toilet_path, blank=True, null=True)
    additional = models.CharField(max_length=200, null=True, default=None, blank=True)
    interior_photos = models.FileField(upload_to=user_interior_path, blank=True, null=True)

LIGHT_CHOICES = (
    ('l01', 'встроенные точечные светильники (обеспечивают основное равномерное освещение)'),
    ('l02', 'накладные точечные споты (в зависимости от типа лампы обеспечивают равномерное или акцентное освещение)'),
    ('l03', 'светодиодная подсветка потолка (освещение для создания уютной атмосферы)'),
    ('l04', 'светодиодная подсветка стен, ниш, мебели (освещение для создания уютной атмосферы)'),
    ('l05', 'трековое освещение - встроенное\накладное (в зависимости от типа светильника используется в разных видах освещения)'),
    ('l06', 'подвесные светильники (в зависимости от типа плафона обеспечивают функциональное освещение поверхностей или рассеивают свет)'),
    ('l07', 'потолочные светильники ("люстры") (как общее, так и декоративное освещение)'),
    ('l08', 'настенные светильники (бра)'),
    ('l09', 'светильники, которые включаются в розетку (напольные и настольные лампы)'),
    ('l10', 'Другое:'),
)

TEMP_CHOICES = (
    ('l01', '6000К холодный цвет (используется в основном в больших пространствах типа музеев, торговых центров и т.д.)'),
    ('l02', '4000-4500К нейтральный цвет (оптимально для общего освещения в квартирах и офисах)'),
    ('l03', '3000К теплый цвет (чаще используется в подсветках, торшерах и других источниках света, создающих уютную атмосферу)'),
    ('l04', 'Другое:'),
)


class Light(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lights = MultiSelectField(choices=LIGHT_CHOICES, default=None, null=True, blank=True)
    lights_other = models.CharField(max_length=200, null=True, default=None, blank=True)
    temperature = MultiSelectField(choices=TEMP_CHOICES, default=None, null=True, blank=True)
    temp_other = models.CharField(max_length=200, null=True, default=None, blank=True)




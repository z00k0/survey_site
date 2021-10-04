from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class User(AbstractUser):
    pass

class Personal(models.Model):
    def user_media_path(instance, filename):
        return 'upload/user_{0}/plan/{1}'.format(instance.user.id, filename)
    user = models.OneToOneField(User, on_delete=CASCADE)
    name = models.CharField(max_length=50)
    survey_date = models.DateTimeField(auto_now_add=True, db_index=True)
    addr = models.TextField(blank=True, default=None)
    square = models.FloatField(default=0)
    plan = models.ImageField(upload_to=user_media_path)
    interests = models.CharField(max_length=500)
    budget = models.FloatField(default=0)
    # equip_cat = [
    #     ('All', ''),
    #     ('Part', ''),
    #     ('Most', '')
    # ]
    # project_style = models.CharField()
    # beauty = models.CharField()


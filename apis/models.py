from django.db import models
import django
from django.contrib.auth.models import User
import datetime
# Create your models here.

class BandUser(models.Model):
    bu_user = models.OneToOneField(User, null=True)
    bu_band = models.IntegerField(default=0)
    bu_openid = models.CharField(max_length=128)
    bu_gender = models.IntegerField(default=0)  # 1 = male 2 = female
    bu_birthday = models.DateTimeField(default=django.utils.timezone.now)
    bu_height = models.IntegerField(default=160)  # cm
    bu_weight = models.IntegerField(default=55)  # kg
    bu_follow = models.ManyToManyField(User, related_name='bu_follow')
    bu_plan = models.IntegerField(default=-1)

class Tree(models.Model):
    user = models.OneToOneField(BandUser, unique=True)
    height = models.FloatField(default=10)
    health = models.IntegerField(default=10)


class HistoryPlan(models.Model):
    hp_id = models.AutoField(primary_key=True, unique=True)
    hp_user = models.ForeignKey(User, related_name='hp_user')
    hp_date = models.DateField()
    hp_plan = models.IntegerField()


class Step(models.Model):
    st_id = models.AutoField(primary_key=True, unique=True)
    st_user = models.ForeignKey(BandUser, null=True, related_name="steps")
    st_time = models.DateTimeField(default=django.utils.timezone.now)
    st_date = models.IntegerField(default=0)
    st_step_number = models.IntegerField(default=0)
    st_calorie = models.IntegerField(default=0)
    st_distance = models.IntegerField(default=0)


class TagContent(models.Model):
    tc_id = models.AutoField(primary_key=True, unique=True)
    tc_user = models.ForeignKey(BandUser, related_name='tc_user')
    tc_content = models.CharField(max_length=128)


class Tag(models.Model):
    tg_id = models.AutoField(primary_key=True, unique=True)
    tg_user = models.ForeignKey(BandUser, related_name='tg_user')
    tg_time_from = models.DateTimeField()
    tg_time_to = models.DateTimeField()
    tg_content = models.ForeignKey(TagContent, related_name='tag')


class Plan(models.Model):
    pl_id = models.AutoField(primary_key=True, unique=True)
    pl_user = models.ForeignKey(BandUser, related_name='plans')
    pl_time_from = models.DateTimeField(default=django.utils.timezone.now)
    pl_time_to = models.DateTimeField(default=django.utils.timezone.now)
    pl_goal = models.CharField(max_length=128)
    pl_description = models.TextField(max_length=256)
    status = models.BooleanField(default=False)


class Health(models.Model):
    he_id = models.AutoField(primary_key=True, unique=True)
    he_user = models.ForeignKey(User, related_name='he_user')
    he_time = models.DateTimeField()
    he_pressure = models.IntegerField()
    he_heart_rate = models.IntegerField()


class Sleep(models.Model):
    sl_id = models.AutoField(primary_key=True, unique=True)
    sl_user = models.ForeignKey(User, related_name='sl_user')
    sl_time_from = models.DateTimeField()
    sl_time_to = models.DateTimeField()
    sl_length = models.TimeField()
    sl_deep_length = models.TimeField()


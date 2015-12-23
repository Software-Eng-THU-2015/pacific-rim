from django.db import models
import django
from django.contrib.auth.models import User
import datetime
# Create your models here.


class BandUser(models.Model):
    bu_band = models.IntegerField(default=0)
    bu_openid = models.CharField(max_length=128)
    bu_gender = models.IntegerField(default=0)  # 1 = male 2 = female
    bu_birthday = models.DateTimeField(default=django.utils.timezone.now)
    bu_height = models.IntegerField(default=160)  # cm
    bu_weight = models.IntegerField(default=55)  # kg
    bu_follow = models.ManyToManyField(User, related_name='bu_follow')
    bu_plan = models.IntegerField(default=-1)
    bu_today_done = models.BooleanField(default=False)
    bu_tree_height = models.FloatField(default=0)
    bu_tree_health = models.IntegerField(default=10)
    bu_tree_today_watertime = models.IntegerField(default=0)
    bu_tree_today_fertilizer = models.IntegerField(default=0)


class HistoryPlan(models.Model):
    hp_id = models.AutoField(primary_key=True, unique=True)
    hp_openid = models.ForeignKey(BandUser, related_name='hp_openid')
    hp_date = models.DateField()
    hp_plan = models.IntegerField()


class Step(models.Model):
    st_id = models.AutoField(primary_key=True, unique=True)
    st_openid = models.ForeignKey(BandUser, related_name='st_openid')
    st_start_time = models.DateTimeField(default=django.utils.timezone.now)
    st_step_number = models.IntegerField()
    st_calorie = models.IntegerField()
    st_distance = models.IntegerField()


class TagContent(models.Model):
    tc_id = models.AutoField(primary_key=True, unique=True)
    tc_openid = models.ForeignKey(BandUser, related_name='tc_openid')
    tc_content = models.CharField(max_length=128)


class Tag(models.Model):
    tg_id = models.AutoField(primary_key=True, unique=True)
    tg_openid = models.ForeignKey(BandUser, related_name='tg_openid')
    tg_time_from = models.DateTimeField()
    tg_time_to = models.DateTimeField()
    tg_content = models.ForeignKey(TagContent, related_name='tag')


class Plan(models.Model):
    pl_id = models.AutoField(primary_key=True, unique=True)
    pl_openid = models.ForeignKey(BandUser, related_name='pl_openid')
    pl_time_from = models.DateTimeField()
    pl_time_to = models.DateTimeField()
    pl_time = models.TimeField()
    pl_goal = models.CharField(max_length=128)
    pl_description = models.TextField()


class Health(models.Model):
    he_id = models.AutoField(primary_key=True, unique=True)
    he_user = models.ForeignKey(BandUser, related_name='he_user')
    he_time = models.DateTimeField()
    he_pressure = models.IntegerField()
    he_heart_rate = models.IntegerField()


class Sleep(models.Model):
    sl_id = models.AutoField(primary_key=True, unique=True)
    sl_openid = models.ForeignKey(BandUser, related_name='sl_openid')
    sl_time_from = models.DateTimeField()
    sl_time_to = models.DateTimeField()
    sl_length = models.TimeField()
    sl_deep_length = models.TimeField()

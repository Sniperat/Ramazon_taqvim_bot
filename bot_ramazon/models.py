from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=50)
    time = models.TimeField(auto_now=False)
    is_plus = models.SmallIntegerField(default=0)
    reg_bamdod = models.TimeField(auto_now=False, null=True)
    reg_tong = models.TimeField(auto_now=False, null=True)
    reg_peshin = models.TimeField(auto_now=False, null=True)
    reg_asr = models.TimeField(auto_now=False, null=True)
    reg_shom = models.TimeField(auto_now=False, null=True)
    reg_xufton = models.TimeField(auto_now=False, null=True)


class User(models.Model):
    telegram_user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=50, default=None, null=True)
    region_ID = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, default=None)
    note_babdod = models.SmallIntegerField(default=0)
    note_tong = models.SmallIntegerField(default=0)
    note_peshin = models.SmallIntegerField(default=0)
    note_asr = models.SmallIntegerField(default=0)
    note_shom = models.SmallIntegerField(default=0)
    note_xufton = models.SmallIntegerField(default=0)


class Namoz(models.Model):
    bamdod = models.TimeField(auto_now=False)
    tong = models.TimeField(auto_now=False)
    peshin = models.TimeField(auto_now=False)
    asr = models.TimeField(auto_now=False)
    shom = models.TimeField(auto_now=False)
    xufton = models.TimeField(auto_now=False)


class Duolar(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()

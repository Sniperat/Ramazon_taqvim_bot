from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=50)
    time = models.CharField(max_length=5)


class User(models.Model):
    telegram_user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=50, default=None, null=True)
    region_ID = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, default=None)

from django.db import models


class User(models.Model):
    telegram_user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=50, default=None, null=True)
    region = models.CharField(max_length=5, default=None, null=True)



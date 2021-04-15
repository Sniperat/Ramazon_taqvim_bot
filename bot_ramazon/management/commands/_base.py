from telegram.ext import Updater
from django.core.management.base import BaseCommand


class BotBase(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(BotBase, self).__init__(*args, **kwargs)


        self.updater = Updater("1776123695:AAEL6j47PcQWE60bIQw2znNWtfc2cYKdOuw")
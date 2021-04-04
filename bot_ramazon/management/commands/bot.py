from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters, RegexHandler, MessageHandler
from ._base import BotBase
import json, requests
import datetime
from ...functions import user_func

api = 'https://api.aladhan.com/timingsByAddress?address=Tashkent,%20UK&method=99&methodSettings=18.5,null,17.5'
response = requests.get(api)
# print(response.json())

time = json.dumps(response.json())
print(time)
print(datetime.datetime.now())


class Command(BotBase):



    def start(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)

        keyboard = [
            [
                InlineKeyboardButton('Курси', callback_data='course'),
                InlineKeyboardButton('Интенсивы', callback_data='2')
            ],

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text("Salam", reply_markup=reply_markup)


    def handle(self, *args, **kwargs):
        dispatcher = self.updater.dispatcher

        # dispatcher.add_handler(CallbackQueryHandler(self.days2, pattern="^(\d{4}\-\d{2}\-\d{2})$"))

        # dispatcher.add_handler(CallbackQueryHandler(self.main_me, pattern="^(main)$"))
        # dispatcher.add_handler(CallbackQueryHandler(self.about, pattern="^(about)$"))
        # dispatcher.add_handler(CallbackQueryHandler(self.course, pattern="^(course)$"))
        # dispatcher.add_handler(CallbackQueryHandler(self.course1, pattern="^(course1)$"))
        # dispatcher.add_handler(CallbackQueryHandler(self.money, pattern="^(money)$"))
        dispatcher.add_handler(CommandHandler('start', self.start))
        # dispatcher.add_handler(CallbackQueryHandler(self.button))

        # dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, self.message_handler))

        self.updater.start_polling()
        self.updater.idle()

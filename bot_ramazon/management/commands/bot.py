from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters, RegexHandler, MessageHandler
from ._base import BotBase
import json, requests
import datetime
from ...functions import user_func
from ...models import Region

api = 'https://api.aladhan.com/timingsByAddress?address=Tashkent,%20UK&method=99&methodSettings=18.5,null,17.5'
response = requests.get(api)
time = response.json()


# print(time)
# print(datetime.datetime.now())
taqvim = time['data']['timings']
kun = time['data']['date']['readable']




class Command(BotBase):



    def start(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)

        keyboard = [
            [
                InlineKeyboardButton('Manzilni tanlash', callback_data='region')
            ],

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text("Assalamu aleykum va rahmatullohu va barokatuhu\nAniq vaqt uchun o'z manzilingizni belgilang", reply_markup=reply_markup)

    def region(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        region = Region.objects.all()
        query = update.callback_query
        query.answer()
        keyboard = []

        for i in region:
            keyboard.append([
                InlineKeyboardButton(i.name, callback_data=i.id)
            ],)

        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text='Manzilni tanlash', reply_markup=reply_markup)
    def button(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        query = update.callback_query
        query.answer()
        region = Region.objects.get(id=query.data)
        keyboard = []
        if str(query.data) == str(region.id):
            user.region_ID = region
            user.save()
            keyboard = [
                [
                    InlineKeyboardButton("Economy", callback_data='comnE')

                ],
                [
                    InlineKeyboardButton("Standart", callback_data='comnS')

                ],
                [
                    InlineKeyboardButton("Deluxe", callback_data='comnD')

                ],
                [
                    InlineKeyboardButton("Luxe", callback_data='comnL')

                ],
                [
                    InlineKeyboardButton("Назад", callback_data='asd')

                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            query.edit_message_text(text='asda', reply_markup=reply_markup)
    def handle(self, *args, **kwargs):
        dispatcher = self.updater.dispatcher

        # dispatcher.add_handler(CallbackQueryHandler(self.days2, pattern="^(\d{4}\-\d{2}\-\d{2})$"))

        # dispatcher.add_handler(CallbackQueryHandler(self.main_me, pattern="^(main)$"))
        # dispatcher.add_handler(CallbackQueryHandler(self.about, pattern="^(about)$"))
        # dispatcher.add_handler(CallbackQueryHandler(self.course, pattern="^(course)$"))
        # dispatcher.add_handler(CallbackQueryHandler(self.course1, pattern="^(course1)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.region, pattern="^(region)$"))
        dispatcher.add_handler(CommandHandler('start', self.start))
        dispatcher.add_handler(CallbackQueryHandler(self.button))

        # dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, self.message_handler))

        self.updater.start_polling()
        self.updater.idle()

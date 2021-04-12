from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters, RegexHandler, MessageHandler
from ._base import BotBase
import json, requests
import datetime
from ...functions import user_func, notification_change
from ...models import Region, Namoz, Duolar
from bs4 import BeautifulSoup


page = requests.get('https://islam.uz/')
soup = BeautifulSoup(page.content, 'html.parser')
html = list(soup.children)[0]
body = list(html.children)[3]
mody = list(body.children)[1]
pody = list(mody.children)[3]
hody = list(pody.children)[1]
lody = list(hody.children)[11]
endd = list(lody.children)[3]
dsadsa = list(endd.children)[1]
misa = list(dsadsa.children)[1]
final = misa.get_text()
array = final.split('\n')
newList = []
for i in array:
    if i == '':
        pass
    else:
        newList.append(i)

asd = datetime.time(int(newList[2][:2]), int(newList[2][3:]))
namoz = Namoz.objects.get(id=1)
namoz.bamdod = datetime.time(int(newList[2][:2]), int(newList[2][3:]))
namoz.tong = datetime.time(int(newList[6][:2]), int(newList[6][3:]))
namoz.peshin = datetime.time(int(newList[9][:2]), int(newList[9][3:]))
namoz.asr = datetime.time(int(newList[12][:2]), int(newList[12][3:]))
namoz.shom = datetime.time(int(newList[15][:2]), int(newList[15][3:]))
namoz.xufton = datetime.time(int(newList[18][:2]), int(newList[18][3:]))
# namoz = Namoz(bamdod=datetime.time(int(newList[2][:2]), int(newList[2][3:])),
#               tong=datetime.time(int(newList[6][:2]), int(newList[6][3:])),
#               peshin=datetime.time(int(newList[9][:2]), int(newList[9][3:])),
#               asr=datetime.time(int(newList[12][:2]), int(newList[12][3:])),
#               shom=datetime.time(int(newList[15][:2]), int(newList[15][3:])),
#               xufton=datetime.time(int(newList[18][:2]), int(newList[18][3:]))
#               )
namoz.save()



def addSecs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()


class Command(BotBase):

    def start(self, update: Update, context: CallbackContext) -> None:
        print(update.message.chat_id)
        user = user_func(update)

        keyboard = [
            [
                InlineKeyboardButton("Manzilni tanlash", callback_data='sta'),
            ],

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text("Assalom", reply_markup=reply_markup)

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

    def asd(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        query = update.callback_query
        query.answer()
        keyboard = [
            [
                InlineKeyboardButton('nazad', callback_data='back')
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="🏙saharlik vaqti: {}\n🌄Iftorlik vaqti: {}\n{} vaqti bilan kamida {} daqiqa qo'shilgan".format(user.region_ID.reg_bamdod,
                                                                                                                        user.region_ID.reg_shom ,
                                                                                                                        user.region_ID.name,
                                                                                                                        user.region_ID.time), reply_markup=reply_markup)

    def button(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        query = update.callback_query
        query.answer()


        try:
            region = Region.objects.get(id=query.data)
        except:
            region = None


        keyboard = []
        if region != None:
            if str(query.data) == str(region.id):
                user.region_ID = region
                user.save()
                keyboard = [
                    [
                        InlineKeyboardButton("Namoz vaqtlari", callback_data='times')
                    ],
                    [
                        InlineKeyboardButton("saharlik vaqti", callback_data='asd'),
                        InlineKeyboardButton("iftorlik vaqti", callback_data='asd')
                    ],
                    [
                        InlineKeyboardButton("Ogohlantirishlarni yoqish", callback_data='notifi')
                    ],
                    [
                        InlineKeyboardButton("Duolar", callback_data='duo')
                    ]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                query.edit_message_text(text='asda', reply_markup=reply_markup)
        if str(query.data[:3]) == 'duo':
            id = query.data[3:]
            duo = Duolar.objects.get(id=int(id))

            keyboard = [
                [
                    InlineKeyboardButton("Nazad", callback_data='duo')
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            query.edit_message_text(text=duo.content, reply_markup=reply_markup)

        if str(query.data[:12]) == 'notification':
            key = query.data[12:]
            notification_change(user, key)

            keyboard = [
                [
                    InlineKeyboardButton(f"Bomdod {'❌' if user.note_babdod == 0 else '✅'}",
                                         callback_data='notification1'),
                    InlineKeyboardButton(f"Peshin {'❌' if user.note_peshin == 0 else '✅'}",
                                         callback_data='notification2')
                ],
                [
                    InlineKeyboardButton(f"Asr {'❌' if user.note_asr == 0 else '✅'}", callback_data='notification3'),
                    InlineKeyboardButton(f"Shom {'❌' if user.note_shom == 0 else '✅'}", callback_data='notification4')
                ],

                [
                    InlineKeyboardButton(f"Xufton {'❌' if user.note_xufton == 0 else '✅'}",
                                         callback_data='notification5')
                ],
                [
                    InlineKeyboardButton('Back', callback_data='back')
                ]

            ]

            reply_markup = InlineKeyboardMarkup(keyboard)
            query.edit_message_text(text='Siz buyerda namoz vaqtlarini kelganda eslatib turish funksiyasini'
                                         'yoqishingiz mumkun', reply_markup=reply_markup)
        if query.data[:6] == 'rememb':
            num = int(query.data[7:])
            if num == 1:
                user.note_time = 10
            if num == 5:
                user.note_time = 5
            if num == 0:
                user.note_time = 0
            if num == 2:
                user.note_time = 20
            user.save()
            self.notifi(update, context)


    def back(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        query = update.callback_query
        query.answer()

        keyboard = [
            [
                InlineKeyboardButton("Namoz vaqtlari", callback_data='times')
            ],
            [
                InlineKeyboardButton("saharlik vaqti", callback_data='asd'),
                InlineKeyboardButton("iftorlik vaqti", callback_data='asd')
            ],
            [
                InlineKeyboardButton("Ogohlantirishlarni yoqish", callback_data='notifi')
            ],
            [
                InlineKeyboardButton("Duolar", callback_data='duo')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text='asda', reply_markup=reply_markup)

    def times(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        query = update.callback_query
        query.answer()
        keyboard = [
            [
                InlineKeyboardButton("Back", callback_data='back')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text=f'Bamdod  {user.region_ID.reg_bamdod}\n'
                                     f'Peshin  {user.region_ID.reg_peshin}\n'
                                     f'Asr-----{user.region_ID.reg_asr}\n'
                                     f'Shom    {user.region_ID.reg_shom}\n'
                                     f'Xufton  {user.region_ID.reg_xufton}', reply_markup=reply_markup)

    def duo(self, update: Update, context: CallbackContext) -> None:
        duo = Duolar.objects.all()
        user = user_func(update)

        namoz = Namoz.objects.get(id=1)
        query = update.callback_query
        query.answer()
        keyboard = []
        for i in duo:
            keyboard.append([
                InlineKeyboardButton(i.name, callback_data='duo'+str(i.id))
            ], )
        keyboard.append([
            InlineKeyboardButton('back', callback_data='back')
        ], )
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text='Duolar', reply_markup=reply_markup)

    def duoin(self, update: Update, context: CallbackContext) -> None:
        duo = Duolar.objects.all()
        user = user_func(update)

        namoz = Namoz.objects.get(id=1)
        query = update.callback_query
        query.answer()
        id =query.data[2:]

        keyboard = []
        for i in duo:
            keyboard.append([
                InlineKeyboardButton(i.name, callback_data='duo'+i.id)
            ], )
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text='Duolar', reply_markup=reply_markup)

    def notifi(self, update: Update, context: CallbackContext) -> None:
        duo = Duolar.objects.all()
        user = user_func(update)

        namoz = Namoz.objects.get(id=1)
        query = update.callback_query
        query.answer()
        id = query.data[2:]


        keyboard = [
            [
                InlineKeyboardButton('notification', callback_data='notification')
            ],
            [
                InlineKeyboardButton(user.note_time+' daqiqa oldin eslat', callback_data='remember')
            ],
            [
                InlineKeyboardButton('ortga', callback_data='back')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text='Duolar', reply_markup=reply_markup)

    def remember(self, update: Update, context: CallbackContext) -> None:
        duo = Duolar.objects.all()
        user = user_func(update)

        namoz = Namoz.objects.get(id=1)
        query = update.callback_query
        query.answer()
        id = query.data[2:]


        keyboard = [
            [
                InlineKeyboardButton('0', callback_data='rememb-0'),
                InlineKeyboardButton('5', callback_data='rememb-5')
            ],
            [
                InlineKeyboardButton(' 10', callback_data='rememb-1'),
                InlineKeyboardButton(' 20', callback_data='rememb-2')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text='Duolar', reply_markup=reply_markup)

    def notification(self, update: Update, context: CallbackContext) -> None:
        duo = Duolar.objects.all()
        user = user_func(update)

        namoz = Namoz.objects.get(id=1)
        query = update.callback_query
        query.answer()
        id =query.data[2:]

        keyboard = [
            [
                InlineKeyboardButton(f"Bomdod {'❌' if user.note_babdod == 0 else '✅'}", callback_data='notification1'),
                InlineKeyboardButton(f"Peshin {'❌' if user.note_peshin == 0 else '✅'}", callback_data='notification2')
            ],
            [
                InlineKeyboardButton(f"Asr {'❌' if user.note_asr == 0 else '✅'}", callback_data='notification3'),
                InlineKeyboardButton(f"Shom {'❌' if user.note_shom == 0 else '✅'}", callback_data='notification4')
            ],
            [
                InlineKeyboardButton(f"Xufton {'❌' if user.note_xufton == 0 else '✅'}", callback_data='notification5')
            ],
            [
                InlineKeyboardButton('Back', callback_data='back')
            ]

        ]


        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text='Siz buyerda namoz vaqtlarini kelganda eslatib turish funksiyasini'
                                     'yoqishingiz mumkun', reply_markup=reply_markup)

    def handle(self, *args, **kwargs):
        dispatcher = self.updater.dispatcher

        # dispatcher.add_handler(CallbackQueryHandler(self.days2, pattern="^(\d{4}\-\d{2}\-\d{2})$"))
        dispatcher.add_handler(CallbackQueryHandler(self.remember, pattern="^(\{6}\-\d{1})$"))

        # dispatcher.add_handler(CallbackQueryHandler(self.main_me, pattern="^(main)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.region, pattern=f"^(sta)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.back, pattern="^(back)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.asd, pattern="^(asd)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.times, pattern="^(times)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.duo, pattern="^(duo)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.notification, pattern="^(notification)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.notifi, pattern="^(notifi)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.remember, pattern="^(remember)$"))
        dispatcher.add_handler(CommandHandler('start', self.start))
        dispatcher.add_handler(CallbackQueryHandler(self.button))

        # dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, self.message_handler))

        self.updater.start_polling()
        self.updater.idle()

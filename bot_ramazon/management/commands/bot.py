from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Filters, RegexHandler, \
    MessageHandler
from typing import List

from ._base import BotBase
import json, requests
import datetime
from ...functions import user_func, notification_change, get_month
from ...models import Region, Duolar, User
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

map_a = []
list_a = []
for ji in Region.objects.all():
    list_a.append(ji)

    if len(list_a)>1:
        # list_a.remove(list_a[0])
        map_a.append((list(list_a), list_a[0]))


def addSecs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()


class Command(BotBase):

    def start(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)

        keyboard = [
            [
                InlineKeyboardButton("Манзилни танлаш", callback_data='sta'),
            ],

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\nУшбу ботимиз муборак '
                                  'Рамазон ойида сизга янгилик бўлади деган умиддамиз.\n', reply_markup=reply_markup)

    def region(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        region = Region.objects.all()
        query = update.callback_query
        query.answer()
        objects = {}
        all = []
        new_list = [region[i:i+3] for i in range(0, len(region), 2)]
        temp = []
        keyboard = []
        for i in new_list:
            for y in i:
                temp.append(InlineKeyboardButton(y.name, callback_data=y.id))
            keyboard.append(temp)
            temp = []
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text='Илтимос, ўзингиз истиқомат қилаётган шаҳарни танланг\n\nШаҳар '
                                     'танлаганингиздан сўнг Тақвим автоматик тарзда шу шаҳар вақтига ўзгаради  '
                                     '\n\n*Эслатма: '
                                     'Танланган шаҳарни `Созламалар` бўлимида ўзгартиришингиз мумкин.',
                                reply_markup=reply_markup)

    def saxar(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        query = update.callback_query
        query.answer()
        keyboard = [
            [
                InlineKeyboardButton('Ўзбекча \uD83C\uDDFA\uD83C\uDDFF', callback_data='yopish_uz')
            ],
            [
                InlineKeyboardButton('Орқага ◀️', callback_data='back')
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="🏙 Саҳарлик: {}\n\n\uD83E\uDD32 Оғиз ёпиш дуоси: Навайту ан асума совма шахри "
                                     "рамазона минал фажри илал "
                                     'мағриби, холисан лиллахи таъала.'
                                     'Аллоҳу акбар!\n\n'
                                     '🏡 Танланган шаҳар: {}  '
                                .format(user.region_ID.reg_bamdod,
                                        user.region_ID.name), reply_markup=reply_markup)

    def iftor(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        query = update.callback_query
        query.answer()
        keyboard = [
            [
                InlineKeyboardButton('Ўзбекча \uD83C\uDDFA\uD83C\uDDFF', callback_data='ochish_uz')
            ],
            [
                InlineKeyboardButton('Орқага ◀️', callback_data='back')
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="🌄 Ифторлик: {}\n\n\uD83E\uDD32 Оғиз очиш дуоси: Аллоҳумма лака сумту ва бика "
                                     "аманту ва "'ъалайка таваккалту ва ъала ризқика афтарту, '
                                     'фағфирли ва ғоффарума қоддамту ва ма аххорту. Амийн\n\n'
                                     '🏡 Танланган шаҳар: {}  '
                                .format(user.region_ID.reg_shom,
                                        user.region_ID.name), reply_markup=reply_markup)

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
                        InlineKeyboardButton("Намоз вақтлари", callback_data='times')
                    ],
                    [
                        InlineKeyboardButton("Саҳарлик вақти", callback_data='saxar'),
                        InlineKeyboardButton("Ифторлик вақти", callback_data='iftor')
                    ],
                    [
                        InlineKeyboardButton("Созламалар", callback_data='notifi')
                    ],
                    [
                        InlineKeyboardButton("Дуолар", callback_data='duo')
                    ]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                query.edit_message_text(text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                             '🗓 Бугун: {} {}\n'
                                             '🏢 Танланган шаҳар: {}\n\n'
                                             'Ушбу ботимиз муборак '
                                             'Рамазон ойида сизга янгилик бўлади деган умиддамиз.\n'.format(
                    datetime.datetime.now().date().day,get_month(datetime.datetime.now().date().month) ,user.region_ID.name),
                    reply_markup=reply_markup)

        if str(query.data[:3]) == 'duo':
            id = query.data[3:]
            duo = Duolar.objects.get(id=int(id))

            keyboard = [
                [
                    InlineKeyboardButton("Орқага ◀️", callback_data='duo')
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            query.edit_message_text(text=duo.content, reply_markup=reply_markup)

        if str(query.data[:12]) == 'notification':
            key = query.data[12:]
            notification_change(user, key)

            keyboard = [
                [
                    InlineKeyboardButton(f"Бомдод {'❌' if user.note_bamdod == 0 else '✅'}",
                                         callback_data='notification1'),
                    InlineKeyboardButton(f"Пешин {'❌' if user.note_peshin == 0 else '✅'}",
                                         callback_data='notification2')
                ],
                [
                    InlineKeyboardButton(f"Аср {'❌' if user.note_asr == 0 else '✅'}", callback_data='notification3'),
                    InlineKeyboardButton(f"Шом {'❌' if user.note_shom == 0 else '✅'}", callback_data='notification4')
                ],

                [
                    InlineKeyboardButton(f"Хуфтон {'❌' if user.note_xufton == 0 else '✅'}",
                                         callback_data='notification5')
                ],
                [
                    InlineKeyboardButton('Орқага ◀️', callback_data='notifi')
                ]

            ]

            reply_markup = InlineKeyboardMarkup(keyboard)
            query.edit_message_text(text='Сиз бу ерда намоз вақтлари яқинлашганда эслатиб туриш функциясини'
                                         'ёқишингиз мумкин.', reply_markup=reply_markup)
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
                InlineKeyboardButton("Намоз вақтлари", callback_data='times')
            ],
            [
                InlineKeyboardButton("Саҳарлик вақти", callback_data='saxar'),
                InlineKeyboardButton("Ифторлик вақти", callback_data='iftor')
            ],
            [
                InlineKeyboardButton("Созламалар", callback_data='notifi')
            ],
            [
                InlineKeyboardButton("Дуолар", callback_data='duo')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     '🗓 Бугун: {} {}\n'
                                     '🏢 Танланган шаҳар: {}\n\n'
                                     'Ушбу ботимиз муборак '
                                     'Рамазон ойида сизга янгилик бўлади деган умиддамиз.\n'.format(
            datetime.datetime.now().date().day, get_month(datetime.datetime.now().date().month), user.region_ID.name),
            reply_markup=reply_markup)

    def times(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        query = update.callback_query
        query.answer()
        keyboard = [
            [
                InlineKeyboardButton("Орқага ◀️", callback_data='back')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text=f'{user.region_ID.name} шаҳрида бугунги намоз вақтлари\n\n' +
                                     f'🔹 Бомдод     {user.region_ID.reg_bamdod}\n\n'
                                     f'🔹 Пешин      {user.region_ID.reg_peshin}\n\n'
                                     f'🔹 Аср            {user.region_ID.reg_asr}\n\n'
                                     f'🔹 Шом          {user.region_ID.reg_shom}\n\n'
                                     f'🔹 Хуфтон       {user.region_ID.reg_xufton}', reply_markup=reply_markup)

    def duo(self, update: Update, context: CallbackContext) -> None:
        duo = Duolar.objects.all()
        user = user_func(update)

        query = update.callback_query
        query.answer()
        keyboard = []
        for i in duo:
            keyboard.append([
                InlineKeyboardButton(i.name, callback_data='duo' + str(i.id))
            ], )
        keyboard.append([
            InlineKeyboardButton('Орқага ◀️', callback_data='back')
        ], )
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text='Дуолар', reply_markup=reply_markup)

    def duoin(self, update: Update, context: CallbackContext) -> None:
        duo = Duolar.objects.all()
        user = user_func(update)

        query = update.callback_query
        query.answer()
        id = query.data[2:]

        keyboard = []
        for i in duo:
            keyboard.append([
                InlineKeyboardButton(i.name, callback_data='duo' + i.id)
            ], )
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text='Дуолар', reply_markup=reply_markup)

    def notifi(self, update: Update, context: CallbackContext) -> None:
        duo = Duolar.objects.all()
        user = user_func(update)

        query = update.callback_query
        query.answer()
        id = query.data[2:]

        keyboard = [
            [
                InlineKeyboardButton('Эслатмалар', callback_data='notification')
            ],
            [
                InlineKeyboardButton('Эслатма вақтлари', callback_data='remember')
            ],
            [
                InlineKeyboardButton("Шаҳарни ўзгартириш", callback_data='sta')
            ],
            [
                InlineKeyboardButton('Орқага ◀️', callback_data='back')
            ]

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(
            text='Танланган эслатма вақти: ' + user.note_time + '\nТанланган шаҳар: ' + user.region_ID.name,
            reply_markup=reply_markup)

    def remember(self, update: Update, context: CallbackContext) -> None:
        duo = Duolar.objects.all()
        user = user_func(update)

        query = update.callback_query
        query.answer()
        id = query.data[2:]

        keyboard = [
            [
                InlineKeyboardButton('0', callback_data='rememb-0'),
                InlineKeyboardButton('5 Дақиқа', callback_data='rememb-5'),
                InlineKeyboardButton('10 Дақиқа', callback_data='rememb-1'),
                InlineKeyboardButton('20 Дақиқа', callback_data='rememb-2')
            ],
            [
                InlineKeyboardButton('Орқага ◀️', callback_data='notifi')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text='Эслатма вақтини тангланг. \n\n', reply_markup=reply_markup)

    def notification(self, update: Update, context: CallbackContext) -> None:
        duo = Duolar.objects.all()
        user = user_func(update)

        query = update.callback_query
        query.answer()
        id = query.data[2:]

        keyboard = [
            [
                InlineKeyboardButton(f"Бомдод {'❌' if user.note_bamdod == 0 else '✅'}", callback_data='notification1'),
                InlineKeyboardButton(f"Пешин {'❌' if user.note_peshin == 0 else '✅'}", callback_data='notification2')
            ],
            [
                InlineKeyboardButton(f"Аср {'❌' if user.note_asr == 0 else '✅'}", callback_data='notification3'),
                InlineKeyboardButton(f"Шом {'❌' if user.note_shom == 0 else '✅'}", callback_data='notification4')
            ],
            [
                InlineKeyboardButton(f"Хуфтон {'❌' if user.note_xufton == 0 else '✅'}", callback_data='notification5')
            ],
            [
                InlineKeyboardButton('Орқага ◀️', callback_data='notifi')
            ]

        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text='Сиз бу ерда намоз вақтлари яқинлашганда эслатиб туриш функциясини'
                                     'ёқишингиз мумкин', reply_markup=reply_markup)

    def delete(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        query.answer()
        query.delete_message()

    def ochish_uz(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        query = update.callback_query
        query.answer()
        keyboard = [
            [
                InlineKeyboardButton('Арабча \uD83C\uDDE6\uD83C\uDDEA', callback_data='iftor')
            ],
            [
                InlineKeyboardButton('Орқага ◀️', callback_data='back')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text='🌄 Ифторлик: {}\n\n\uD83E\uDD32 Оғиз очиш дуоси: Эй Аллоҳ, ушбу рўзамни Сен '
                                     'учун тутдим ва Сенга иймон келтирдим ва Сенга '
                                     'таваккал қилдим ва берган ризқинг билан ифтор қилдим. Эй гуноҳларни афв '
                                     'қилувчи Зот, менинг аввалги ва кейинги гуноҳларимни мағфират қилгил. Амийн\n\n'
                                     '🏡 Танланган шаҳар: {}  '
                                .format(user.region_ID.reg_shom,
                                        user.region_ID.name), reply_markup=reply_markup)


    def yopish_uz(self, update: Update, context: CallbackContext) -> None:
        user = user_func(update)
        query = update.callback_query
        query.answer()
        keyboard = [
            [
                InlineKeyboardButton('Арабча \uD83C\uDDE6\uD83C\uDDEA', callback_data='saxar')
            ],
            [
                InlineKeyboardButton('Орқага ◀️', callback_data='back')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text='🏙 Саҳарлик: {}\n\n\uD83E\uDD32 Оғиз ёпиш дуоси: Аллоҳ таоло учун ихлос билан '
                                     'тонгдан то офтоб ботгунича рамазон '
                                     'ойининг рўзасини тутмоқликни ният қилдим. Аллоҳу акбар\n\n'
                                     '🏡 Танланган шаҳар: {}  '
                                .format(user.region_ID.reg_bamdod,
                                        user.region_ID.name), reply_markup=reply_markup)

    def handle(self, *args, **kwargs):
        dispatcher = self.updater.dispatcher

        # dispatcher.add_handler(CallbackQueryHandler(self.days2, pattern="^(\d{4}\-\d{2}\-\d{2})$"))
        dispatcher.add_handler(CallbackQueryHandler(self.remember, pattern="^(\{6}\-\d{1})$"))

        # dispatcher.add_handler(CallbackQueryHandler(self.main_me, pattern="^(main)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.region, pattern=f"^(sta)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.back, pattern="^(back)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.saxar, pattern="^(saxar)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.iftor, pattern="^(iftor)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.times, pattern="^(times)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.duo, pattern="^(duo)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.notification, pattern="^(notification)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.notifi, pattern="^(notifi)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.remember, pattern="^(remember)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.delete, pattern="^(delete)$"))
        # dispatcher.add_handler(CallbackQueryHandler(self.ochish, pattern="^(ochish)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.ochish_uz, pattern="^(ochish_uz)$"))
        # dispatcher.add_handler(CallbackQueryHandler(self.yopish, pattern="^(yopish)$"))
        dispatcher.add_handler(CallbackQueryHandler(self.yopish_uz, pattern="^(yopish_uz)$"))
        dispatcher.add_handler(CommandHandler('start', self.start))
        dispatcher.add_handler(CallbackQueryHandler(self.button))

        # dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, self.message_handler))

        self.updater.start_polling()
        self.updater.idle()

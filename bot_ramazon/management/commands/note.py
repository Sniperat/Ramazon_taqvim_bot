from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext
from ...models import Region, Namoz, Duolar, User
from ._base import BotBase
import json, requests
import datetime
from bs4 import BeautifulSoup
from ...functions import user_func, notification_change


def addSecs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()


def removeSecs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate - datetime.timedelta(seconds=secs)
    return fulldate.time()


class Command(BotBase):
    def handle(self, *args, **options):
        main_hour = datetime.datetime.now().time().hour
        main_minut = datetime.datetime.now().time().minute
        regions = Region.objects.all()
        if datetime.timedelta(hours=main_hour, minutes=main_minut) == (datetime.timedelta(hours=0, minutes=1) or
                                                                       datetime.timedelta(hours=0, minutes=5) or
                                                                       datetime.timedelta(hours=0, minutes=30)):
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
            region = Region.objects.all()


            bamdod = datetime.time(int(newList[2][:2]), int(newList[2][3:]))
            tong = datetime.time(int(newList[6][:2]), int(newList[6][3:]))
            peshin = datetime.time(int(newList[9][:2]), int(newList[9][3:]))
            asr = datetime.time(int(newList[12][:2]), int(newList[12][3:]))
            shom = datetime.time(int(newList[15][:2]), int(newList[15][3:]))
            xufton = datetime.time(int(newList[18][:2]), int(newList[18][3:]))

            for reg in region:
                minute = str(reg.time)[3:-3]
                seconde = str(reg.time)[6:]
                timeseconds = int(minute) * 60 + int(seconde)
                if reg.is_plus == 0:
                    reg.reg_bamdod = addSecs(bamdod, timeseconds)
                    reg.reg_tong = addSecs(tong, timeseconds)
                    reg.reg_peshin = addSecs(peshin, timeseconds)
                    reg.reg_asr = addSecs(asr, timeseconds)
                    reg.reg_shom = addSecs(shom, timeseconds)
                    reg.reg_xufton = addSecs(xufton, timeseconds)
                if reg.is_plus == 1:
                    reg.reg_bamdod = removeSecs(bamdod, timeseconds)
                    reg.reg_tong = removeSecs(tong, timeseconds)
                    reg.reg_peshin = removeSecs(peshin, timeseconds)
                    reg.reg_asr = removeSecs(asr, timeseconds)
                    reg.reg_shom = removeSecs(shom, timeseconds)
                    reg.reg_xufton = removeSecs(xufton, timeseconds)
                reg.save()
        keyboard = [
            [
                InlineKeyboardButton("Yopish", callback_data='delete'),
            ],

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        for u in regions:
            # todo Bamdod vaqtlari
            redate = removeSecs(u.reg_bamdod, 20 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_bamdod=1, note_time=20)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Бомдод вақтига {} дақиқа қолди'.format(i.note_time),
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            redate = removeSecs(u.reg_bamdod, 10 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_bamdod=1, note_time=10)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Бомдод вақтига {} дақиқа қолди'.format(i.note_time),
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            redate = removeSecs(u.reg_bamdod, 5 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_bamdod=1, note_time=5)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Бомдод вақтига {} дақиқа қолди'.format(i.note_time),
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            hour = u.reg_bamdod.hour
            minut = u.reg_bamdod.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_bamdod=1, note_time=0)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Бомдод вақти бўлди',
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            # todo Tong vaqtlari
            redate = removeSecs(u.reg_tong, 20 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                pass
            redate = removeSecs(u.reg_tong, 10 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                pass
            redate = removeSecs(u.reg_tong, 5 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                pass
            hour = u.reg_tong.hour
            minut = u.reg_tong.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                pass
            # todo Peshin vaqtlari
            redate = removeSecs(u.reg_peshin, 20 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.get(note_peshin=1, note_time=20)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Пешин вақтига {} дақиқа қолди'.format(i.note_time),
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            redate = removeSecs(u.reg_peshin, 10 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_peshin=1, note_time=10)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Пешин вақтига {} дақиқа қолди'.format(i.note_time),
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            redate = removeSecs(u.reg_peshin, 5 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_peshin=1, note_time=5)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Пешин вақтига {} дақиқа қолди'.format(i.note_time),
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            hour = u.reg_peshin.hour
            minut = u.reg_peshin.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_peshin=1, note_time=0)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Пешин вақти бўлди',
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            # todo Asr vaqtlari
            redate = removeSecs(u.reg_asr, 20 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_asr=1, note_time=20)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Аср вақтига {} дақиқа қолди'.format(i.note_time),
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            redate = removeSecs(u.reg_asr, 10 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_asr=1, note_time=10)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Аср вақтига {} дақиқа қолди'.format(i.note_time),
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            redate = removeSecs(u.reg_asr, 5 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):

                users = User.objects.filter(note_asr=1, note_time=5)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Аср вақтига {} дақиқа қолди'.format(i.note_time),
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            hour = u.reg_asr.hour
            minut = u.reg_asr.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_asr=1, note_time=0)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Аср вақти бўлди',
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            # todo Shom vaqtlari
            redate = removeSecs(u.reg_shom, 20 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_shom=1, note_time=20)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Шом вақтига {} дақиқа қолди'.format(i.note_time),
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            redate = removeSecs(u.reg_shom, 10 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_shom=1, note_time=10)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Шом вақтига {} дақиқа қолди'.format(i.note_time),
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            redate = removeSecs(u.reg_shom, 5 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_shom=1, note_time=5)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Шом вақтига {} дақиқа қолди'.format(i.note_time),
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            hour = u.reg_shom.hour
            minut = u.reg_shom.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_shom=1, note_time=0)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Шом вақти бўлди',
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            # todo Xufton vaqtlari
            redate = removeSecs(u.reg_xufton, 20 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_xufton=1, note_time=20)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Хуфтон вақтига {} дақиқа қолди'.format(i.note_time),
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            redate = removeSecs(u.reg_xufton, 10 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_xufton=1, note_time=10)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Хуфтон вақтига {} дақиқа қолди'.format(i.note_time),
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            redate = removeSecs(u.reg_xufton, 5 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_xufton=1, note_time=5)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Хуфтон вақтига {} дақиқа қолди'.format(i.note_time),
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

            hour = u.reg_xufton.hour
            minut = u.reg_xufton.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_xufton=1, note_time=0)
                for i in users:
                    if i.region_ID == u:
                        try:
                            self.updater.bot.send_message(
                                chat_id=i.telegram_user_id,
                                text='Ассаламуалайкум ва роҳматуллоҳу ва баракату! \n\n'
                                     'Хуфтон вақти бўлди',
                                reply_markup=reply_markup)
                        except Exception as e:
                            i.delete()

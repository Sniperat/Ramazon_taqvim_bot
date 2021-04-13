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
        if datetime.timedelta(hours=main_hour, minutes=main_minut) == datetime.timedelta(hours=1, minutes=00):
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
        for i in regions:
            # todo Bamdod vaqtlari
            redate = removeSecs(i.reg_bamdod, 20 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_bamdod=1, note_time=20)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Bamdod namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )


            redate = removeSecs(i.reg_bamdod, 10 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_bamdod=1, note_time=10)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Bamdod namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )
            redate = removeSecs(i.reg_bamdod, 5 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_bamdod=1, note_time=5)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Bamdod namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )
            hour = i.reg_bamdod.hour
            minut = i.reg_bamdod.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_bamdod=1, note_time=0)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Bamdod namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )
            # todo Tong vaqtlari
            redate = removeSecs(i.reg_tong, 20 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                pass
            redate = removeSecs(i.reg_tong, 10 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                pass
            redate = removeSecs(i.reg_tong, 5 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                pass
            hour = i.reg_tong.hour
            minut = i.reg_tong.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                pass
            # todo Peshin vaqtlari
            redate = removeSecs(i.reg_peshin, 20 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.get(note_peshin=1, note_time=20)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Peshin namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )
            redate = removeSecs(i.reg_peshin, 10 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_peshin=1, note_time=10)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Peshin namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )
            redate = removeSecs(i.reg_peshin, 5 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_peshin=1, note_time=5)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Peshin namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )
            hour = i.reg_peshin.hour
            minut = i.reg_peshin.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_peshin=1, note_time=0)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Peshin namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )
            # todo Asr vaqtlari
            redate = removeSecs(i.reg_asr, 20 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_asr=1, note_time=20)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Asr namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )
            redate = removeSecs(i.reg_asr, 10 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_asr=1, note_time=10)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Asr namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )
            redate = removeSecs(i.reg_asr, 5 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):

                users = User.objects.filter(note_asr=1, note_time=5)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Asr namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )
            hour = i.reg_asr.hour
            minut = i.reg_asr.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_asr=1, note_time=0)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Asr namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )

            # todo Shom vaqtlari
            redate = removeSecs(i.reg_shom, 20 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_shom=1, note_time=20)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Shom namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )
            redate = removeSecs(i.reg_shom, 10 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_shom=1, note_time=10)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Shom namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )
            redate = removeSecs(i.reg_shom, 5 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_shom=1, note_time=5)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Shom namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )
            hour = i.reg_shom.hour
            minut = i.reg_shom.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_shom=1, note_time=0)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Shom namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )

            # todo Xufton vaqtlari
            redate = removeSecs(i.reg_xufton, 20 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_xufton=1, note_time=20)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Xufton namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )
            redate = removeSecs(i.reg_xufton, 10 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_xufton=1, note_time=10)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Xufton namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )
            redate = removeSecs(i.reg_xufton, 5 * 60)
            hour = redate.hour
            minut = redate.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_xufton=1, note_time=5)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Xufton namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )
            hour = i.reg_xufton.hour
            minut = i.reg_xufton.minute
            if datetime.timedelta(hours=main_hour,
                                  minutes=main_minut) == datetime.timedelta(hours=hour,
                                                                            minutes=minut):
                users = User.objects.filter(note_xufton=1, note_time=0)
                for i in users:
                    try:
                        self.updater.bot.send_message(
                            chat_id=i.telegram_user_id,
                            text='Xufton namoziga {} daqiqa vaqt qoldi'.format(i.note_time),
                            reply_markup=reply_markup)
                    except Exception as e:
                        self.updater.bot.send_message(
                            chat_id=920393608,
                            text="TID: {}, user:{},\n\n{}".format(i.telegram_user_id, i.user_name, str(e))
                        )

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
                print(i)
                newList.append(i)

        asd = datetime.time(int(newList[2][:2]), int(newList[2][3:]))
        # namoz = Namoz.objects.get(id=1)
        # namoz.bamdod = datetime.time(int(newList[2][:2]), int(newList[2][3:]))
        # namoz.tong = datetime.time(int(newList[6][:2]), int(newList[6][3:]))
        # namoz.peshin = datetime.time(int(newList[9][:2]), int(newList[9][3:]))
        # namoz.asr = datetime.time(int(newList[12][:2]), int(newList[12][3:]))
        # namoz.shom = datetime.time(int(newList[15][:2]), int(newList[15][3:]))
        # namoz.xufton = datetime.time(int(newList[18][:2]), int(newList[18][3:]))
        # namoz = Namoz(bamdod=datetime.time(int(newList[2][:2]), int(newList[2][3:])),
        #               tong=datetime.time(int(newList[6][:2]), int(newList[6][3:])),
        #               peshin=datetime.time(int(newList[9][:2]), int(newList[9][3:])),
        #               asr=datetime.time(int(newList[12][:2]), int(newList[12][3:])),
        #               shom=datetime.time(int(newList[15][:2]), int(newList[15][3:])),
        #               xufton=datetime.time(int(newList[18][:2]), int(newList[18][3:]))
        #               )
        # namoz.save()
        region = Region.objects.all()
        print('apchuus')
        user = User.objects.all()
        # userTime = user.region_ID.time
        # minute = str(userTime)[3:-3]
        # seconde = str(userTime)[6:]
        # timeseconds = int(minute) * 60 + int(seconde)

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

        # if datetime.datetime.now().time() == datetime.timedelta(hours=17, minutes=40):
        for row in User.objects.all():
            try:
                self.updater.bot.send_message(
                    chat_id=row.telegram_user_id,
                    text='hello mf'
                )
            except Exception as e:
                self.updater.bot.send_message(
                    chat_id=920393608,
                    text="TID: {}, ID:{}, NAME: {}\n\n{}".format(row.id, row.telegram_user_id, row.first_name, str(e))
                )

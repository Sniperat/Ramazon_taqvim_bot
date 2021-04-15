from .models import User
import datetime


def user_func(update):
    try:
        user = User.objects.get(telegram_user_id=update.effective_user.id)
    except:
        user = User(telegram_user_id=update.effective_user.id, user_name=update.effective_user.name,
                    telegram_user_id1=update.effective_user.id, first_name=update.effective_user.first_name,
                    last_name=update.effective_user.last_name)
        user.save()
    return user


def get_month(num):
    month = {
        1: 'январь',
        2: 'февраль',
        3: 'март',
        4: 'aпрель',
        5: 'май',
        6: 'июнь',
        7: 'июль',
        8: 'август',
        9: 'сентябрь',
        10: 'октябрь ',
        11: 'ноябрь',
        12: 'декабрь',
    }
    return month[num]

def notification_change(user: User, key):
    if key == '1':
        if user.note_bamdod == 1:
            user.note_bamdod = 0
        else:
            user.note_bamdod = 1
    elif key == '2':
        if user.note_peshin == 1:
            user.note_peshin = 0
        else:
            user.note_peshin = 1
    elif key == '3':
        if user.note_asr == 1:
            user.note_asr = 0
        else:
            user.note_asr = 1
    elif key == '4':
        if user.note_shom == 1:
            user.note_shom = 0
        else:
            user.note_shom = 1
    elif key == '5':
        if user.note_xufton == 1:
            user.note_xufton = 0
        else:
            user.note_xufton = 1
    user.save()
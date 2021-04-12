from .models import User
import datetime


def user_func(update):
    try:
        user = User.objects.get(telegram_user_id=update.effective_user.id)
    except:
        user = User(telegram_user_id=update.effective_user.id, user_name=update.effective_user.name)
        user.save()
    return user

def notification_change(user:User, key):
    if key == '1':
        if user.note_babdod == 1:
            user.note_babdod = 0
        else:
            user.note_babdod = 1
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



def getTime():
    time_string = "01:01:09"

    date_time = datetime.datetime.strptime(time_string, "%H:%M:%S")

    print(date_time)

    a_timedelta = date_time - datetime.datetime(1900, 1, 1)
    seconds = a_timedelta.total_seconds()

    print(seconds)

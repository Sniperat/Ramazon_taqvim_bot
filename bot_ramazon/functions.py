from .models import User


def user_func(update):
    try:
        user = User.objects.get(telegram_user_id=update.effective_user.id)
    except:
        user = User(telegram_user_id=update.effective_user.id, user_name=update.effective_user.name)
        user.save()
    return user

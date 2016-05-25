import random, string, os

_notif_count = 0

def password(length=10):
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    random.seed = (os.urandom(1024))
    password = ''.join(random.choice(chars) for i in range(length))
    return password

def get_notification_id():
    global _notif_count
    _notif_count += 1
    return _notif_count


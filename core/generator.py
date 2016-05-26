import random, string, os

_chars = string.ascii_uppercase + string.digits + string.ascii_lowercase

def password(length=10):
    random.seed = os.urandom(1024)
    password = ''.join(random.choice(_chars) for _ in xrange(length))
    return password

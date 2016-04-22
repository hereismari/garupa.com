import random, string, os

class Generator(object):

    def password(self, length=10):
        chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
        random.seed = (os.urandom(1024))
        password = ''.join(random.choice(chars) for i in range(length))
        return password

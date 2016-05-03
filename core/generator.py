import random, string, os

class Generator(object):
    count = 0
	
    def password(self, length=10):
        chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
        random.seed = (os.urandom(1024))
        password = ''.join(random.choice(chars) for i in range(length))
        return password
       
    def get_notification_id(self):
		self.count += 1
		return self.count
		

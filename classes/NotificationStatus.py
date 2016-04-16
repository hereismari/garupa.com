from enum import Enum

@unique
class NotificationStatus(Enum):

    new = 1
    seen = 2

    def __str__(self):
        return 'status name: %s, status number: %d' % (self.name, self.value)


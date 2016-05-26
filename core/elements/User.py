
class User(object):

    def __init__(self, uid, passwd, name, email):

        self._name = name
        self._uid = uid
        self._email = email
        self._password = passwd

        self._photo = '/assets/img/default-profile-pic.png'
        self._phone = 'N/A'

        self._friends = set()
        self._notifications = []
        self._rides = []

    def __eq__(self, other):
        if type(other) is not User: return False
        return self._uid == other.get_uid()

    def __hash__(self):
        return self._uid


    def has_friend(self, user):
        return user in self._friends

    def add_friend(self, user):
        self._friends.add(user)

    def remove_friend(self, user):
        self._friends.remove(user)

    def get_relationship(self, other):
        self_has_other = self.has_friend(other)
        other_has_self = other.has_friend(self)

        if self == other: rel = 'self'
        elif not self_has_other and not other_has_self: rel = 'none'
        elif     self_has_other and not other_has_self: rel = 'available'
        elif not self_has_other and     other_has_self: rel = 'pending'
        else: rel = 'friend'

        return rel


    def add_notification(self, notification):
        self._notifications.append(notification)

    def remove_notification(self, nid):
        self._notifications = [n for n in self._notifications if n.get_nid() != nid]


    def add_ride(self, ride):
        if ride not in self._rides:
            self._rides.append(ride)

    def remove_ride(self, ride):
        self._rides.remove(ride)

    def update_rides(self):
        self._rides = [r for r in self._rides if r.update()]


    def set_name(self, name):
        self._name = name

    def set_email(self, email):
        self._email = email

    def set_phone(self, phone):
        self._phone = phone

    def se_photo(self, photo):
        self._photo = photo

    def set_password(self, password):
        self._password = password


    def get_uid(self):
        return self._uid

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def get_notifications(self):
        return self._notifications


    def get_view(self, other):
        rel = self.get_relationship(other)
        if rel not in ['self', 'friend']: result = self.get_public_view()
        else: result = self.get_private_view()

        result['relationship'] = rel
        return result

    def get_public_view(self):
        return {
            'name' : self._name,
            'uid' : self._uid,
            'photo' : self._photo
        }

    def get_private_view(self):
        self.update_rides()
        view = self.get_public_view()

        return dict(view, **{
            'email': self._email,
            'phone': self._phone,
            'rides': [r.get_view() for r in self._rides]
        })

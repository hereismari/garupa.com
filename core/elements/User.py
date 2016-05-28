from core.database import db

friendship = db.Table('friendship',
    db.Column('uid_a', db.Integer, db.ForeignKey('user.uid')),
    db.Column('uid_b', db.Integer, db.ForeignKey('user.uid'))
)

user_ride = db.Table('user_ride',
    db.Column('uid', db.Integer, db.ForeignKey('user.uid')),
    db.Column('rid', db.Integer, db.ForeignKey('ride.rid'))
)

class User(db.Model):

    _uid = db.Column('uid', db.Integer, primary_key=True)
    _password = db.Column(db.String(50))

    _name = db.Column(db.String(30))
    _email = db.Column(db.String(30))
    _phone = db.Column(db.String(30))

    _photo = db.Column(db.Text)

    _friends = db.relationship('User',
        secondary='friendship',
        primaryjoin=_uid==friendship.c.uid_a,
        secondaryjoin=_uid==friendship.c.uid_b
    )

    _rides = db.relationship('Ride', secondary='user_ride')
    _notifications = db.relationship('Notification')


    def __init__(self, uid, passwd, name, email):

        self._uid = uid
        self._password = passwd
        self._name = name
        self._email = email

        self._photo = '/assets/img/default-profile-pic.png'
        self._phone = 'N/A'

    def __eq__(self, other):
        if type(other) is not User: return False
        return self._uid == other.get_uid()

    def __hash__(self):
        return self._uid


    def has_friend(self, user):
        return user in self._friends

    def add_friend(self, user):
        self._friends.append(user)

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

    def remove_notification(self, notification):
        self._notifications.remove(notification)


    def add_ride(self, ride):
        self._rides.append(ride)

    def remove_ride(self, ride):
        self._rides.remove(ride)

    def update_rides(self):
        for r in self._rides:
            if not r.update():
                db.session.delete(r)
        db.session.commit()


    def set_name(self, name):
        self._name = name

    def set_email(self, email):
        self._email = email

    def set_phone(self, phone):
        self._phone = phone

    def set_photo(self, photo):
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

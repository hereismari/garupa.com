from core.database import db

class Passenger(db.Model):

    _pid = db.Column('pid', db.Integer, primary_key=True)
    _ride = db.Column(db.ForeignKey('ride.rid'))

    _user = db.relationship('User')
    _user_id = db.Column(db.ForeignKey('user.uid'))

    _district = db.Column(db.String(30))
    _complement = db.Column(db.String(30))

    def __init__(self, user, district, complement):
        self._user = user
        self._district = district
        self._complement = complement

    def get_user(self):
        return self._user

    def get_district(self):
        return self._district

    def get_complement(self):
        return self._complement

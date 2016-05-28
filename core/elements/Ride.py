from time import mktime
from datetime import date, timedelta
from core.database import db
from Passenger import Passenger

class Ride(db.Model):

    _rid = db.Column('rid', db.Integer, primary_key=True)

    _driver = db.relationship('User')
    _driver_id = db.Column(db.ForeignKey('user.uid'))

    _seats = db.Column(db.Integer)

    _date = db.Column(db.DateTime)
    _weekly = db.Column(db.Boolean)

    _dest = db.Column(db.String(10))
    _origin = db.Column(db.String(30))
    _route = db.Column(db.PickleType)

    _passengers = db.relationship('Passenger')

    def __init__(self, driver, date, dest, origin, route, weekly, seats):

        self._driver = driver
        self._seats = seats

        self._date = date
        self._weekly = weekly

        self._dest = dest
        self._origin = origin
        self._route = route

    def __eq__(self, other):
        if type(other) is not Ride: return False
        return self._rid == other.get_rid()

    def __hash__(self):
        return self._rid

    def add_passenger(self, user, district, complement):
        passenger = Passenger(user, district, complement)

        if not self.is_full() and not self.contains_user(user):
            self._passengers.append(passenger)

    def remove_passenger(self, passenger):
        self._passengers.remove(passenger)

    def contains_user(self, user):
        for passenger in self._passengers:
            if passenger.get_user() == user: return True
        return user == self._driver

    def is_full(self):
        return self.get_vacancies() == 0

    def update(self):
        sunday = self.last_sunday()
        if self.is_weekly() and self._date.date() < sunday:
            self._date += timedelta(weeks=1)
        return self._date.date() >= sunday

    def last_sunday(self):
        today = date.today()
        weekday = today.isoweekday() % 7
        return today - timedelta(weekday)

    def happens_on(self, date):
        return abs(self._date - date) <= timedelta(minutes=15)

    def get_vacancies(self):
        return self._seats - len(self._passengers)

    def get_date(self):
        return self._date

    def get_timestamp(self):
        return mktime(self.get_date().timetuple())

    def get_driver(self):
        return self._driver

    def is_weekly(self):
        return self._weekly

    def get_passengers(self):
        return self._passengers

    def get_rid(self):
        return self._rid

    def get_destination(self):
        return self._dest

    def get_origin(self):
        return self._origin

    def get_route(self):
        return self._route

    def get_view(self):
        return {
            'date': int(self.get_timestamp() * 1000),

            'rid': self._rid,
            'driver': self._driver.get_public_view(),
            'dest': self._dest,
            'origin': self._origin,
            'route': self._route,
            'weekly': self._weekly,
            'seats': self.get_vacancies(),

            'passengers': [{
                'name': p.get_user().get_name(),
                'uid': p.get_user().get_uid(),
                'address': {
                    'district': p.get_district(),
                    'complement': p.get_complement()
                }
            } for p in self._passengers]
        }

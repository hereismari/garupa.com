from time import mktime
from datetime import date, timedelta

class Ride(object):

    # variavel estatica
    rid_counter = 1

    def __init__(self, driver, date, dest, origin, route, weekly, seats):

        self._driver = driver
        self._seats = seats

        self._rid = Ride.rid_counter
        Ride.rid_counter += 1

        self._date = date
        self._weekly = weekly

        self._dest = dest
        self._origin = origin
        self._route = route

        self._passengers = []

    def __eq__(self, other):
        if type(other) is not Ride: return False
        return self._rid == other.get_rid()

    def __hash__(self):
        return self._rid

    def add_passenger(self, passenger, address):
        if not self.is_full() and not self.contains_user(passenger):
            self._passengers.append((passenger, address))

    def remove_passenger(self, passenger):
        old_size = self.get_vacancies()

        self._passengers = [p for p in self._passengers if p[0] != passenger]
        return old_size != self.get_vacancies()

    def contains_user(self, user):
        for passenger in self._passengers:
            if passenger[0] == user: return True
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
                'name': p[0].get_name(),
                'uid': p[0].get_uid(),
                'address': {
                    'district': p[1].get_district(),
                    'complement': p[1].get_complement()
                }
            } for p in self.get_passengers()]
        }

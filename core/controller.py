from src import User, Ride, Address
from src import FriendRequestNotification, NewFriendNotification
from datetime import datetime

class Controller(object):

    users = dict()
    rides = dict()

    def get_user(self, uid):
        return self.users.get(uid, None)

    def get_ride(self, uid):
        return self.rides.get(uid, None)

    def recover_passwd(self, uid, new_passwd):
        u = self.get_user(uid)
        if u == None: return False

        u.set_password(new_passwd)
        return True

    def register_user(self, uid, passwd, name, email):
        if uid in self.users: return None
        self.users[uid] = User(uid, passwd, name, email)
        return self.get_user(uid)

    def get_credentials(self, uid):
        u = self.get_user(uid)
        if u == None: return None
        return u.get_password()

    def view_user(self, uid, vuid):
        u = self.get_user(uid)
        v = self.get_user(vuid)

        if u == None or v == None: return None
        return u.get_view(v)

    def update_user(self, uid, attr, value):
        u = self.get_user(uid)
        if u == None: return False

        if attr == 'name': u.set_name(value)
        elif attr == 'email': u.set_email(value)
        elif attr == 'photo': u.set_photo(value)
        elif attr == 'phone': u.set_phone(value)

        else: return False
        return True

    def add_friend(self, uid, fuid):
        u = self.get_user(uid)
        f = self.get_user(fuid)

        if u == None or f == None:
            return False

        u.add_friend(f)
        relation = f.get_relationship(u)

        if relation == 'pending':
            notification = FriendRequestNotification(uid)
            f.add_notification(notification)
        elif relation == 'friend':
            notification = NewFriendNotification(uid)
            f.add_notification(notification)

        return True

    def remove_friend(self, uid, fuid):
        u = self.get_user(uid)
        f = self.get_user(fuid)

        if u == None or f == None:
            return False

        u.remove_friend(f)
        return True

    def get_notifications(self, uid):
        u = self.get_user(uid)

        if u == None:
            return None

        return [n.get_view() for n in u.get_notifications()]

    def join_ride(self, uid, rid, district, complement):
        u = self.get_user(uid)
        r = self.get_ride(rid)

        if u == None or r == None: return False
        if r.is_full(): return False

        address = Address(district, complement)
        r.add_passenger(u, address)
        u.add_ride(r)
        return True

    def cancel_ride(self, uid, rid):
        u = self.get_user(uid)
        r = self.get_ride(rid)

        if u == None or r == None:
            return False

        u.removeRide(r)
        if r.getDriver() == u:
            del self.rides[rid]
            for p in r.get_passengers():
                p[0].remove_ride(r)
        else: r.remove_passenger(u)
        return True

    def register_ride(self, driver, date, dest, origin, route, weekly, seats):
        u = self.get_user(driver)
        if u == None: return False

        date = datetime.fromtimestamp(date / 1000)
        r = Ride(u, date, dest, origin, route, weekly, seats)

        u.add_ride(r)
        self.rides[r.get_rid()] = r
        return True

    def update_rides(self):
        self.rides = { rid: r for rid, r in self.rides.iteritems() if r.update() }

    def search_rides(self, dest, district, date, weekly, uid):
        u = self.get_user(uid)
        date = datetime.fromtimestamp(date / 1000)

        self.update_rides()

        return [r.getView() for r in self.rides.itervalues() if
            r.get_destination() == dest and
            district in r.getRoute() and
            r.happens_on(date) and
            r.isWeekly() == weekly and
            not r.containsUser(u)
        ]

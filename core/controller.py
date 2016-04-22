from src import User, Ride, Address
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

        u.setPassword(new_passwd)
        return True

    def register_user(self, uid, passwd, name, email):
        if uid in self.users: return None
        self.users[uid] = User(uid, passwd, name, email)
        return self.get_user(uid)

    def get_credentials(self, uid):
        u = self.get_user(uid)
        if u == None: return None
        return u.getPassword()

    def view_user(self, uid, vuid):
        u = self.get_user(uid)
        v = self.get_user(vuid)

        if u == None or v == None: return None
        return u.getView(v)

    def update_user(self, uid, attr, value):
        u = self.get_user(uid)
        if u == None: return False

        if attr == 'name': u.setName(value)
        elif attr == 'email': u.setEmail(value)
        elif attr == 'photo': u.setPhoto(value)
        elif attr == 'phone': u.setPhone(value)

        else: return False
        return True

    def add_friend(self, uid, fuid):
        u = self.get_user(uid)
        f = self.get_user(fuid)

        if u == None or f == None:
            return False

        u.addFriend(f)
        return True

    def remove_friend(self, uid, fuid):
        u = self.get_user(uid)
        f = self.get_user(fuid)

        if u == None or f == None:
            return False

        u.removeFriend(f)
        return True

    def join_ride(self, uid, rid, district, complement):
        u = self.get_user(uid)
        r = self.get_ride(rid)

        if u == None or r == None: return False
        if r.isFull(): return False

        address = Address(district, complement)
        r.addPassenger(u, address)
        u.addRide(r)
        return True

    def cancel_ride(self, uid, rid):
        u = self.get_user(uid)
        r = self.get_ride(rid)

        if u == None or r == None:
            return False

        u.removeRide(r)
        if r.getDriver() == u:
            del rides[rid]
            for p in r.getPassengers():
                p.removeRide(p)
        else: r.removePassenger(u)
        return True

    def register_ride(self, driver, date, dest, origin, route, weekly, seats):
        u = self.get_user(driver)
        if u == None: return False

        date = datetime.fromtimestamp(date / 1000)
        r = Ride(u, date, dest, origin, route, weekly, seats)

        u.addRide(r)
        self.rides[r.getRid()] = r
        return True

    def update_rides(self):
        self.rides = { rid: r for rid, r in self.rides.iteritems() if r.update() }

    def search_rides(self, dest, district, date, weekly, uid):
        u = self.get_user(uid)
        date = datetime.fromtimestamp(date / 1000)

        self.update_rides()

        return [r.getView() for r in self.rides.itervalues() if
            r.getDestination() == dest and
            district in r.getRoute() and
            r.happensOn(date) and
            r.isWeekly() == weekly and
            not r.containsUser(u)
        ]

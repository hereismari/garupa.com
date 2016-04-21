from src import User, Ride, Address
from datetime import datetime
from generator import Generator

class Controller(object):

    users = dict()
    rides = dict()
    generator = Generator()

    def get_user(self, uid):
        return self.users.get(uid, None)

    def register_user(self, name, uid, email, passwd):
        if uid in self.users.iteritems():
            return False

        if passwd == '': passwd = self.generator.password()
        
        user = User(name, uid, email, passwd)
        self.users[uid] = user
        return True

    def recover_passwd(self, uid):
        if self.get_user(uid) == None: return False
        new_passwd = self.generator.password()
        self.users[uid].setPassword(new_passwd)
        return True

    def view_user(self, uid, vuid):
        u = self.users.get(uid, None)
        v = self.users.get(vuid, None)

        if u == None or v == None: return None
        return u.getView(v)

    def update_user(self, uid, attr, value):
        u = self.users.get(uid, None)
        if u == None: return False

        if attr == 'name': u.setName(value)
        elif attr == 'email': u.setEmail(value)
        elif attr == 'photo': u.setPhoto(value)
        elif attr == 'phone': u.setPhone(value)

        return True

    def add_friend(self, uid, fuid):
        u = self.users.get(uid, None)
        f = self.users.get(fuid, None)

        if u == None or f == None:
            return False

        u.addFriend(f)
        return True

    def remove_friend(self, uid, fuid):
        u = self.users.get(uid, None)
        f = self.users.get(fuid, None)

        if u == None or f == None:
            return False

        u.removeFriend(f)
        return True

    def join_ride(self, uid, rid, district, complement):
        u = self.users.get(uid, None)
        r = self.rides.get(rid, None)

        if u == None or r == None: return False
        if r.isFull(): return False

        address = Address(district, complement)
        r.addPassenger(u, address)
        u.addRide(r)
        return True

    def cancel_ride(self, uid, rid):
        u = self.users.get(uid, None)
        r = self.rides.get(rid, None)

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
        u = self.users.get(driver, None)
        if u == None: return False
        
        date = datetime.fromtimestamp(date / 1000)
        r = Ride(u, date, dest, origin, route, weekly, seats)

        u.addRide(r)
        self.rides[r.getRid()] = r
        return True

    def update_rides(self):
        self.rides = { ride[0] : ride[1] for ride in self.rides.iteritems() if ride[1].update() }

    def search_rides(self, dest, district, date, weekly, uid):
        u = self.users.get(uid, None)
        date = datetime.fromtimestamp(date / 1000)

        self.update_rides()

        return [r.getView() for r in self.rides.itervalues() if
            r.getDestination() == dest and
            district in r.getRoute() and
            r.happensOn(date) and
            r.isWeekly() == weekly and
            not r.containsUser(u)
        ]


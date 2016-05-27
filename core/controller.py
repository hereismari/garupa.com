import notifications
from elements import User, Ride, Address
from datetime import datetime

class Controller(object):

    users = dict()
    rides = dict()

    def get_user(self, uid):
        return self.users.get(uid, None)

    def get_ride(self, rid):
        return self.rides.get(rid, None)

    def get_notification(self, uid, nid):
        u = self.get_user(uid)
        if u == None: return None

        for n in u.get_notifications():
            if n.get_nid() == nid: return n
        return None

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

        relation = f.get_relationship(u)

        if   relation == 'none':      nt = notifications.FriendRequest(u)
        elif relation == 'available': nt = notifications.FriendAccepted(u)
        else:                         nt = None

        if nt: f.add_notification(nt)
        u.add_friend(f)

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

    def remove_notification(self, uid, nid):
        u = self.get_user(uid)

        if u == None:
            return False

        u.remove_notification(nid)
        return True

    def mark_notification(self, uid, nid):
        n = self.get_notification(uid, nid)

        if n == None:
            return False

        n.set_seen()
        return True

    def request_ride(self, uid, rid, district, complement):
        u = self.get_user(uid)
        r = self.get_ride(rid)

        if u == None or r == None: return False
        if r.is_full(): return False

        d = r.get_driver()
        nt = notifications.RideRequest(r, u, district, complement)
        d.add_notification(nt)

        return True

    def accept_ride(self, uid, rid, district, complement):
        u = self.get_user(uid)
        r = self.get_ride(rid)

        if u == None or r == None: return False
        if r.is_full(): return False

        address = Address(district, complement)
        r.add_passenger(u, address)
        u.add_ride(r)

        d = r.get_driver()
        notification = notifications.RideAccepted(r, d)
        u.add_notification(notification)

        return True

    def cancel_ride(self, uid, rid):
        u = self.get_user(uid)
        r = self.get_ride(rid)

        if u == None or r == None:
            return False

        u.remove_ride(r)
        if r.get_driver() == u:
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

        return [r.get_view() for r in self.rides.itervalues() if
            r.get_destination() == dest and
            district in r.get_route() and
            r.happens_on(date) and
            r.is_weekly() == weekly and
            not r.contains_user(u)
        ]

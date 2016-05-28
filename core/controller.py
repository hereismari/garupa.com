import notifications
from elements import User, Ride, Passenger
from datetime import datetime
from database import db

class Controller(object):

    def get_user(self, uid):
        return User.query.get(uid)

    def get_ride(self, rid):
        return Ride.query.get(rid)

    def get_notification(self, uid, nid):
        return notifications.Notification.query.get(nid)

    def recover_passwd(self, uid, new_passwd):
        u = self.get_user(uid)
        if u == None: return False

        u.set_password(new_passwd)
        db.session.commit()
        return True

    def register_user(self, uid, passwd, name, email):
        if self.get_user(uid): return None

        user = User(uid, passwd, name, email)

        db.session.add(user)
        db.session.commit()

        return user

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

        db.session.commit()

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
        db.session.commit()

        return True

    def remove_friend(self, uid, fuid):
        u = self.get_user(uid)
        f = self.get_user(fuid)

        if u == None or f == None:
            return False

        u.remove_friend(f)
        db.session.commit()

        return True

    def get_notifications(self, uid):
        u = self.get_user(uid)

        if u == None:
            return None

        return [n.get_view() for n in u.get_notifications()]

    def remove_notification(self, uid, nid):
        u = self.get_user(uid)
        n = self.get_notification(uid, nid)

        if u == None or n == None:
            return False

        db.session.delete(n)
        db.session.commit()

        return True

    def mark_notification(self, uid, nid):
        n = self.get_notification(uid, nid)

        if n == None:
            return False

        n.set_seen()
        db.session.commit()

        return True

    def request_ride(self, uid, rid, district, complement):
        u = self.get_user(uid)
        r = self.get_ride(rid)

        if u == None or r == None: return False
        if r.is_full(): return False

        d = r.get_driver()
        nt = notifications.RideRequest(r, u, district, complement)
        d.add_notification(nt)

        db.session.commit()

        return True

    def accept_ride(self, uid, rid, district, complement):
        u = self.get_user(uid)
        r = self.get_ride(rid)

        if u == None or r == None: return False
        if r.is_full(): return False

        r.add_passenger(u, district, complement)
        u.add_ride(r)

        d = r.get_driver()
        notification = notifications.RideAccepted(r, d)
        u.add_notification(notification)

        db.session.commit()

        return True

    def cancel_ride(self, uid, rid):
        u = self.get_user(uid)
        r = self.get_ride(rid)

        if u == None or r == None:
            return False

        u.remove_ride(r)
        if r.get_driver() == u:
            for p in r.get_passengers():
                p.get_user().remove_ride(r)
                db.session.delete(p)
        else:
            r.remove_passenger(u)

        db.session.commit()

        return True

    def register_ride(self, driver, date, dest, origin, route, weekly, seats):
        u = self.get_user(driver)
        if u == None: return False

        date = datetime.fromtimestamp(date / 1000)
        r = Ride(u, date, dest, origin, route, weekly, seats)

        u.add_ride(r)

        db.session.add(r)
        db.session.commit()

        return True

    def update_rides(self):
        for r in Ride.query.all():
            if not r.update():
                db.session.delete(r)
        db.session.commit()

    def search_rides(self, dest, district, date, weekly, uid):
        u = self.get_user(uid)
        date = datetime.fromtimestamp(date / 1000)

        self.update_rides()

        result = [r for r in Ride.query.all() if
            r.get_destination() == dest and
            district in r.get_route() and
            r.happens_on(date) and
            r.is_weekly() == weekly and
            not r.contains_user(u)
        ]

        return [r.get_view() for r in result]

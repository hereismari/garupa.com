
# Todos o metodos dessa classe sao temporarios
class Controller(object):

    users = [{
        'name': 'Victor',
        'uid': 114110495,
        'email': 'victor.almeida@ccc.ufcg.edu.br',
        'photo': '/assets/img/default-profile-pic.png',
        'phone': '(83) 99937-6230',
        'friends': [],
        'rides': []
    }]

    ride_count = 0
    rides = []

    def get_user(self, uid):
        for u in self.users:
            if u['uid'] == uid:
                return u
        return None

    def get_ride(self, rid):
        for r in self.rides:
            if r['rid'] == rid:
                return r
        return None

    def register_user(self, name, uid, email, passwd):
        if self.get_user(uid): return False
        self.users.append({
            'name': name,
            'uid': uid,
            'email': email,
            'photo': '/assets/img/default-profile-pic.png',
            'friends': [],
            'rides': []
        })
        return True
        # true se cadstro foi realizado com sucesso
        # false se houve conflito de uid

    def view_user(self, uid, vuid):
        u, v = self.get_user(uid), self.get_user(vuid)
        if u == None or v == None: return None

        result = dict()

        result['uid'] = u.get('uid')
        result['name'] = u.get('name')
        result['photo'] = u.get('photo')

        result['relationship'] = \
            'self' if uid == vuid else \
            'friend' if uid in v['friends'] and vuid in u['friends'] else \
            'pending' if uid in v['friends'] else \
            'available' if vuid in u['friends'] else \
            'none'

        if result['relationship'] in ['self', 'friend']:
            result['email'] = u.get('email', 'N/A')
            result['phone'] = u.get('phone', 'N/A')
            result['rides'] = []
            for r in u.get('rides'):
                r = r.copy()
                r['passengers'] = None
                d = r['driver']
                r['driver'] = {
                    'uid': d['uid'],
                    'name': d['name'],
                    'photo': d['photo'],
                    'phone': d.get('phone', 'N/A')
                }
                result['rides'].append(r)

        return result
        # dict com view completa se forem amigos ou a mesma pessoa
        # dict com view reduzida se nao forem amigos
        # None se uid ou vuid nao estiverem cadastrados
        # obs: dict contem campo com relacionamento

    def update_user(self, uid, attr, value):
        u = self.get_user(uid)
        if u == None: return False
        u[attr] = value
        return True
        # true se usuario existe
        # false caso contrario

    def add_friend(self, uid, fuid):
        u, f = self.get_user(uid), self.get_user(fuid)
        if u == None or f == None: return False
        u['friends'].append(fuid)
        return True
        # true se usuario existe
        # false caso contrario

    def remove_friend(self, uid, fuid):
        u = self.get_user(uid)
        if u == None: return False
        u['friends'].remove(fuid)
        return True
        # true se usuario existe
        # false caso contrario

    def join_ride(self, uid, rid):
        u, r = self.get_user(uid), self.get_ride(rid)
        if u == None or r == None or r['seats'] == 0: return False
        u['rides'].append(r)
        r['passengers'].append(u)
        r['seats'] -= 1
        return True
        # true se usuario e bigu existem
        # false caso contrario

    def cancel_ride(self, uid, rid):
        u, r = self.get_user(uid), self.get_ride(rid)
        if u == None: return False
        u['rides'].remove(r)
        if r['driver'] == u:
            for p in r['passengers']:
                cancel_ride(p['uid'], rid)
        else:
            r['passengers'].remove(u)
            r['seats'] += 1
        return True
        # true se usuario existe
        # false caso contrario

    def register_ride(self, driver, date, dest, origin, route, repeat, seats):
        u = self.get_user(driver)
        if u == None: return False
        ride = {
            'driver': u,
            'date': date,
            'dest': dest,
            'origin': origin,
            'route': route,
            'repeat': repeat,
            'seats': seats,
            'passengers': [],
            'rid': self.ride_count
        }
        u['rides'].append(ride)
        self.rides.append(ride)
        self.ride_count += 1
        return True
        # true se usuario existe
        # false caso contrario

    def search_rides(self, dest, district, date, uid):
        result = list()
        for r in self.rides:
            if dest == r['dest'] and \
            district in r['route'] and \
            date == r['date'] and \
            uid != r['driver']['uid'] and \
            r['seats'] > 0:
                r = r.copy()
                d = r['driver']
                r['driver'] = {
                    'uid': d['uid'],
                    'name': d['name'],
                    'photo': d['photo'],
                    'phone': d.get('phone', 'N/A')
                }
                result.append(r)
        return result

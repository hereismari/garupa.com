
# Todos o metodos dessa classe sao temporarios
class Controller(object):

    users = [{
        'name': 'Victor',
        'uid': 114110495,
        'email': 'victor.almeida@ccc.ufcg.edu.br',
        'phone': '(83) 99937-6230',
        'friends': []
    }]

    def get(self, uid):
        for u in self.users:
            if u['uid'] == uid:
                return u
        return None

    def register(self, name, uid, email, passwd):
        if self.get(uid): return False
        self.users.append({
            'name': name,
            'uid': uid,
            'email': email,
            'friends': []
        })
        return True
        # true se cadstro foi realizado com sucesso
        # false se houve conflito de uid

    def view_user(self, uid, vuid):
        u, v = self.get(uid), self.get(vuid)
        if u == None or v == None: return None

        result = dict()

        result['uid'] = u.get('uid')
        result['name'] = u.get('name')
        result['photo'] = u.get('photo', '/assets/img/default-profile-pic.png')

        result['relationship'] = \
            'self' if uid == vuid else \
            'friend' if uid in v['friends'] and vuid in u['friends'] else \
            'pending' if uid in v['friends'] else \
            'available' if vuid in u['friends'] else \
            'none'

        if result['relationship'] in ['self', 'friend']:
            result['email'] = u.get('email', None)
            result['phone'] = u.get('phone', None)

        return result
        # dict com view completa se forem amigos ou a mesma pessoa
        # dict com view reduzida se nao forem amigos
        # None se uid ou vuid nao estiverem cadastrados
        # obs: dict contem campo com relacionamento

    def update_user(self, uid, attr, value):
        u = self.get(uid)
        if u == None: return False
        u[attr] = value
        return True
        # true se usuario existe
        # false caso contrario

    def add_friend(self, uid, fuid):
        u, f = self.get(uid), self.get(fuid)
        if u == None or f == None: return False
        u['friends'].append(fuid)
        return True
        # true se usuario existe
        # false caso contrario

    def remove_friend(self, uid, fuid):
        u = self.get(uid)
        if u == None: return False
        u['friends'].remove(fuid)
        return True
        # true se usuario existe
        # false caso contrario

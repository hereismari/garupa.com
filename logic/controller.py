
# Todos o metodos dessa classe sao temporarios
class Controller(object):

    users = [{
        'name': 'Victor',
        'id': 114110495,
        'email': 'victor.almeida@ccc.ufcg.edu.br',
        'phone': '(83) 99937-6230'
    }]

    def register(self, name, uid, email, passwd):
        for u in self.users:
            if u['id'] == uid:
                return False
        self.users.append({
            'name': name,
            'id': uid,
            'email': email
        })
        return True
        # true se cadstro foi realizado com sucesso
        # false se houve conflito de uid

    def user_view(self, uid, vid):
        for u in self.users:
            if u['id'] == uid:
                result = u.copy()
                result['relationship'] = 'self'
                return result
        return None
        # dict com view completa se forem amigos ou a mesma pessoa
        # dict com view reduzida se nao forem amigos
        # None se uid nao estiver cadastrado
        # obs: dict contem campo com relacionamento

    def update_user(self, uid, attr, value):
        for u in self.users:
            if u['id'] == uid: u[attr] = value

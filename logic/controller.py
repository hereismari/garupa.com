
# Todos o metodos dessa classe sao temporarios
class Controller(object):

    def register(self, name, uid, email, passwd):
        return True
        # true se cadstro foi realizado com sucesso
        # false se houve conflido de uid

    def user_view(self, uid, vid):
        if uid == 114110495: return {
            'name': 'Victor',
            'id': '114110495',
            'email': 'victor.almeida@ccc.ufcg.edu.br',
            'phone': '(83) 99937-6230',
            'relationship': 'self'
        }

        return None
        # dict com view completa se forem amigos ou a mesma pessoa
        # dict com view reduzida se nao forem amigos
        # None se uid nao estiver cadastrado
        # obs: dict contem campo com relacionamento

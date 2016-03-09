
app.controller('profile', function($scope, $stateParams, Users) {
    $scope.user = Users.get($stateParams.uid);
    $scope.signed = (Users.loggedUser === $scope.user);

    $scope.table = _.map([
        ['Matrícula', 'id',                                                                                    ],
        ['Nome',      'name',    'ie.: Fulaninho da Silva',                    '.{3,}'                         ],
        ['Telefone',  'phone',   'ie.: (83) 99988-1122',                         '\\(\\d\\d\\) \\d{4,5}-\\d{4}'],
        ['Endereço',  'address', 'ie.: Rua Tomé de Souza, 288, José Pinheiro', '.{5,}'                         ],
        ['Email',     'email',   'ie.: fulano.silva@email.com',                '.+@.+\\..+'                    ],
    ],
        function(row) {
            return { name: row[0], data: row[1], placeholder: row[2], pattern: row[3] };
        });
});


app.controller('profile', function($scope, $stateParams, Users) {
    $scope.user = Users.get($stateParams.uid);

    $scope.table = _.map([
        ['Nome',      $scope.user.name   ],
        ['Telefone',  $scope.user.phone  ],
        ['Endereço',  $scope.user.address],
        ['Matrícula', $scope.user.id     ],
        ['Email',     $scope.user.email  ],
        ['Senha',     '**********'       ]
    ],
        function(row) {
            return { name: row[0], data:row[1] };
        });
});


app.controller('profile', function($scope, $stateParams, Users) {
    $scope.user = Users.get($stateParams.uid);
    $scope.signed = (Users.loggedUser === $scope.user);

    $scope.table = _.map([
        ['Nome',      $scope.user.name,    false],
        ['Telefone',  $scope.user.phone,   false],
        ['Endereço',  $scope.user.address, false],
        ['Matrícula', $scope.user.id,      false],
        ['Email',     $scope.user.email,   false],
        ['Senha',     '**********',        true ]
    ],
        function(row) {
            return { name: row[0], data: row[1], secret: row[2] };
        });
});

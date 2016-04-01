
app.controller('profile', function($scope, $stateParams, Users, Districts) {
    $scope.user = Users.get($stateParams.uid);
    $scope.signed = (Users.loggedUser === $scope.user);

    $scope.Districts = Districts;

    $scope.init = function() {
        $('select').select2({
            placeholder: 'Bairro',
            formatNoMatches: 'Nenhum bairro encontrado',
            dropdownCssClass: 'show-select-search'
        });
    };
});

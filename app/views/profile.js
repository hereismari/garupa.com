
app.controller('profile', function($scope, $stateParams, Users) {
    $scope.user = Users.get($stateParams.uid);
    $scope.signed = (Users.loggedUser === $scope.user);
});

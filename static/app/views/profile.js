
app.controller('profile', function($scope, $stateParams, Users, Districts) {
    $scope.user = Users.get($stateParams.uid);
    $scope.signed = (Users.loggedUser === $scope.user);
});

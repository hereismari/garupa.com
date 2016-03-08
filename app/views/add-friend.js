
app.controller('add-friend', function($scope, $stateParams, Users) {
    $scope.user = Users.get($stateParams.uid);
    $scope.loggedUser = Users.loggedUser;
});

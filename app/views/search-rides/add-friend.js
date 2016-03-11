
app.controller('add-friend', function($scope, $stateParams, Users) {
    $scope.user = Users.get($stateParams.uid);

    $scope.state =
        $scope.user.hasFriend(Users.loggedUser)? 'accept':
        Users.loggedUser.hasFriend($scope.user)? 'cancel': 'request';
});
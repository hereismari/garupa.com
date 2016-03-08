
app.controller('add-friend', function($scope, $stateParams, Users) {
    var loggedUser = Users.loggedUser;
    $scope.user = Users.get($stateParams.uid);

	$scope.state =
		$scope.user.hasFriend(loggedUser)? 'accept':
		loggedUser.hasFriend($scope.user)? 'cancel': 'request';
});

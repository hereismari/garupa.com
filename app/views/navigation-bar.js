app.directive('navBar', function() {
  return {
    templateUrl: 'app/views/navigation-bar.html',
    
    controller: function($scope, Users) {
		$scope.user = Users.loggedUser;
		$scope.changeStat = function() {
			$scope.user.loggedUser = !$scope.user.loggedUser;
		};
	}
  };
});

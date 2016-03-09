'use strict';

app.controller('loginAttemptController', function($scope, $routeParams) {
	$scope.log = $routeParams.login_attempt;
});
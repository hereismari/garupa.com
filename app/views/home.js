'use strict';

app.controller('homeController', function($scope, $location) {

	/* My First "Bad smell" */

	$scope.user = {
		username: null,
		password: null
	};

	$scope.form = {
		username: null,
		password: null
	};

	$scope.signUp = function() {
		// cadastrar usuario
	};

	$scope.signIn = function() {
		// logar usuario
	};

});
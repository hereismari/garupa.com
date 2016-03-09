'use strict';

app.controller('homeController', function($scope, $location) {

	$scope.welcome_text = "Bem-vindo ao Garupa.com!";
	$scope.welcome_desc = "Consiga ou ofereça carona para da Universidade e faça novas amizades! ";

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

	$scope.toogleSignUpForm = function() {
		$( "#welcome" ).fadeOut("slow", function() {
			$( ".sign-up" ).fadeIn("slow");
		});
	}

});
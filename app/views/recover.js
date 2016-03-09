'use strict';

app.controller('recoverController', function($scope, $location) {

	// enviar email de recuperação de senha 

	$scope.recoverPasswd = function() {
		$( ".form-recover" ).fadeOut("slow", function() {
			$( ".form-recover-msg" ).fadeIn("slow");
		});
	}

});



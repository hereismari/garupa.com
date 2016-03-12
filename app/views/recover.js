
app.controller('recover', function($scope) {

	// enviar email de recuperação de senha

	$scope.recoverPasswd = function() {
		$('.form-recover').fadeOut('slow', function() {
			$('.form-recover-msg').fadeIn('slow');
		});
	}

});

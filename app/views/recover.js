
app.controller('recover', function($scope) {

	// enviar email de recuperação de senha

	$scope.recover = function() {
		$('#recovery-form').fadeOut('slow', function() {
			$('#form-confirmation').fadeIn('slow');
		});
	};
});

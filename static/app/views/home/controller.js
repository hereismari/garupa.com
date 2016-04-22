
app.controller('home', function($scope, $state, Api) {

	$scope.form = new Object();
	$scope.form.passwd = '';
	
	$scope.toggleForm = function() {
		$('#welcome').fadeOut('slow', function() {
			$('form').fadeIn('slow');
		});
	};

	$scope.submit = function() {
		
        if($scope.generate) $scope.form.passwd = '';
		$scope.form.uid = parseInt($scope.form.uid)

		Api.registerUser($scope.form).then(
			function(resp) {
				alert('Cadastro realizado com sucesso!');
				$state.go('login');
			},

			function(resp) {
				if(resp.status == 409) alert('Matrícula já cadastrada!');
				if(resp.status == 400) alert('Preencha esse negoço direito!');
			});
	};
});

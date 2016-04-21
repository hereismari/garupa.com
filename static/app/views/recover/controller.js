
app.controller('recover', function($scope, $state, Api) {

	$scope.form = new Object();
    
    $scope.recover_passwd = function() {
        
        Api.recover_passwd($scope.form).then(
            function(resp) {
                alert('Um email foi enviado para voce com sua senha');
		        $('#recovery-form').fadeOut('slow', function() {
			        $('#form-confirmation').fadeIn('slow');
		        });
                $state.go('login');
            },
            function(resp) {
                if(resp.status == 409) alert('Email não cadastrado');
                else alert('Oops, tivemos um problema. Verifique se seu email foi digitado corretamente');
            });
    	};
    }
});

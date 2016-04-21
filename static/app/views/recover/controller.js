
app.controller('recover', function($scope, $state, Api) {

    $scope.form = new Object();
    
    $scope.recover_passwd = function() {
	Api.recoverPassword($scope.form.uid).then(
	    function(resp) {
		alert('Um email foi enviado para você com sua senha');
		$state.go('login');
	    },
	    function(resp) {
		if(resp.status == 404) alert('Matrícula não cadastrada :(');
		else alert('Oops, tivemos um problema. Verifique se sua matrícula foi digitado corretamente');
	    });       
    };
});

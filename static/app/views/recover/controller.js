
app.controller('recover', function($scope, $state, $stateParams, Api) {

    $scope.uid = $stateParams.uid;

    $scope.recover = function() {
        Api.recoverPassword($scope.uid).then(
            function(resp) {
                alert('Um email foi enviado para você com sua senha.');
                $state.go('login', { uid: $scope.uid });
            },

            function(resp) {
                if(resp.status == 404) alert('Matrícula não cadastrada.');
                else alert('Oops, tivemos um problema.');
            });
    };
});

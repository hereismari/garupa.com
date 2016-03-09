app.directive('offering', function() {
    return {
        restrict: 'E',
        scope: {ngModel: '='},
        templateUrl: 'app/CarpoolOffering/offering.html',

        controller: function($scope) {
            $scope.carona = {
                partida: 'Casa',
                destino: 'UFCG',
                data: '',
                hora: ''
            }



        }
    }
})

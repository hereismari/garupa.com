app.directive('offering', function() {
    return {
        restrict: 'E',
        scope: {ngModel: '='},
        templateUrl: 'app/CarpoolOffering/offering.html',

        controller: function($scope) {
            $scope.carpool = {
                from: 'Casa',
                to: 'UFCG',
                day: '',
                time: ''
            };

            $scope.$watch('carpool.from', function() {
                $scope.carpool.to = 'UFCG';
            });
        }
    }
});

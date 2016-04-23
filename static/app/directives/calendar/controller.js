
app.directive('calendar', function() {
    return {
        restrict: 'E',
        scope: { user: '=', show: '=' },
        templateUrl: '/app/directives/calendar/template.html',
        css: '/app/directives/calendar/style.css',

        controller: function($scope, Day, Destination, NextWeek) {
            $scope.Day = Day;
            $scope.Destination = Destination;

            $scope.rides = new Array();

            $scope.$watch('user.rides', function(rides) {
                $scope.rides = _.filter(rides, function(ride) {
                    return ride.date < NextWeek;
                });
            });

            $scope.check = function(timestamp, day) {
                return new Date(timestamp).getDay() == day.index;
            };
        }
    }
});

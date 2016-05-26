
app.directive('rideInfo', function($location, Users, Destination) {
    return {
        restrict: 'E',
        scope: { show: '=', frozen: '=' },
        templateUrl: '/app/directives/ride-info/template.html',
        css: '/app/directives/ride-info/style.css',
        replace: true,

        link: function(scope, element) {
            scope.Destination = Destination;

            $(element).modal({
                show: false
            });

            scope.go = function(uid) {
                $(element).modal('hide')
                    .on('hidden.bs.modal', function() {
                        $location.path('/perfil/' + uid);
                        scope.$apply();
                    });
            };

            scope.show = function(ride) {
                scope.ride = ride;
                $(element).modal('show');
            };

            scope.cancelRide = function() {
                Users.logged.cancelRide(scope.ride.rid);
            };
        }
    };
});

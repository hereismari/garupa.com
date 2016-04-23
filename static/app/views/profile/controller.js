
app.controller('profile', function($scope, $stateParams, Users, Districts, Destination, NextWeek) {

    $scope.form = new Object();
    $scope.rides = new Array();

    $scope.Destination = Destination;

    Users.get($stateParams.uid).then(function(user) {
        $scope.user = user;
        $scope.editable = {value: user.relationship == 'self'};
    });

    $scope.$watch('form.photo', function(newValue, oldValue) {
        if(newValue != oldValue) $scope.user.update('photo', newValue);
    });

    $scope.$watch('user.rides', function(rides) {
        $scope.rides = _.filter(rides, function(ride) {
            return ride.date >= NextWeek;
        });
    });

    $scope.removeFriend = function() {
        Users.logged.removeFriend($stateParams.uid).then(function() {
            location.reload();
        });
    };
});

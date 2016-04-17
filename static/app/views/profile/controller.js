
app.controller('profile', function($scope, $stateParams, Users, Districts) {

    $scope.form = new Object();

    Users.get($stateParams.uid).then(function(user) {
        $scope.user = user;
        $scope.editable = {value: user.relationship == 'self'};
    });

    $scope.$watch('form.photo', function(newValue, oldValue) {
        if(newValue != oldValue) $scope.user.update('photo', newValue);
    });

    $scope.removeFriend = function() {
        Users.logged.removeFriend($stateParams.uid).then(function() {
            location.reload();
        });
    };
});

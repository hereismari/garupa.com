
app.controller('profile', function($scope, $stateParams, Users, Districts) {
    Users.get($stateParams.uid).then(function(user) {
        $scope.user = user;
        $scope.editable = {value: user.relationship == 'self'};
    });
});

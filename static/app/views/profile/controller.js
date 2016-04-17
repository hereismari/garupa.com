
app.controller('profile', function($scope, $stateParams, Users, Districts) {
    Users.get($stateParams.uid).then(function(user) {
        $scope.user = user;
        $scope.editable = {value: user.relationship == 'self'};
    });

    $scope.$watch('photo_url', function(newValue, oldValue) {
        if(newValue != oldValue) $scope.user.update('photo_url', newValue);
    });
});

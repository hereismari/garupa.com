
app.controller('add-friend', function($scope, $stateParams, Users) {
    Users.get($stateParams.uid).then(function(user) {
        $scope.user = user;
    });
});

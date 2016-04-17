
app.controller('login', function($scope, $stateParams, $location, Users) {

    $scope.login = function(uid) {
        Users.login(uid).then(function(success) {
            if(success) $location.path($stateParams.redirect);
        });
    };
});

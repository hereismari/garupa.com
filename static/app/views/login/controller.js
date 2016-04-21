
app.controller('login', function($scope, $stateParams, $location, Users) {

    $scope.login = function(uid, passwd) {
        Users.login(uid, passwd).then(function(success) {
            if(success) $location.path($stateParams.redirect);
        });
    };
});

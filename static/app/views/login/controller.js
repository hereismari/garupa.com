
app.controller('login', function($scope, $stateParams, $location, Users) {

    $scope.login = function(uid) {
        if(Users.login(uid)) $location.path($stateParams.redirect);
    };
});

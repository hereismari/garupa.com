
app.controller('login', function($scope, $stateParams, $location, Users) {
    $scope.uid = $stateParams.uid;
    $scope.passwd = null;

    $scope.login = function() {
        Users.login($scope.uid, $scope.passwd).then(function(success) {
            if(success) $location.path($stateParams.redirect);
            else $scope.passwd = null;
        });
    };
});

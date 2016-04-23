
app.controller('add-friend', function($scope, $stateParams, Users) {
    Users.get($stateParams.uid).then(function(user) {
        $scope.user = user;
    });

    $scope.add = function() {
        Users.logged.addFriend($stateParams.uid).then(function() {
            location.reload();
        });
    };

    $scope.cancel = function() {
        Users.logged.removeFriend($stateParams.uid).then(function() {
            location.reload();
        });
    };
});

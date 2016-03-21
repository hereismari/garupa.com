
app.directive('navigationBar', function() {
    return {
        restrict: 'E',
        scope: {},
        templateUrl: 'app/navigation-bar/navigation-bar.html',
        css: 'app/navigation-bar/navigation-bar.css',

        controller: function($scope, $location, Users) {
            $scope.Users = Users;

            $scope.login = function(uid) {
                var success = Users.login(uid);
                $location.path(success? '/perfil' : '/login');
            };

            $scope.logout = function() {
                $location.path('/');
                Users.logout();
            };
        }
    };
});

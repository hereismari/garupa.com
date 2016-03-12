
app.directive('navigationBar', function() {
    return {
        restrict: 'E',
        scope: true,
        templateUrl: 'app/navigation-bar/navigation-bar.html',
        css: 'app/navigation-bar/navigation-bar.css',

        controller: function($scope, $location, Users) {
            $scope.user = Users.loggedUser;

            $scope.login = function(uid) {
                $scope.user = Users.login(uid);
                $location.path($scope.user? '/perfil' : '/login');
            };

            $scope.logout = function() {
                $location.path('/');
                $scope.user = Users.logout();
            }
        }
    };
});

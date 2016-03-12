app.directive('navigationBar', function() {
    return {
        restrict: 'E',
        scope: true,
        templateUrl: 'app/views/navigation-bar.html',
        css: 'app/views/navigation-bar.css',

        controller: function($scope, $location, Users) {
            $scope.user = Users.loggedUser;

            $scope.login = function(uid) {
                $scope.user = Users.login(uid);
                $location.path('/perfil');
            };

            $scope.logout = function() {
                $location.path('/404');
                $scope.user = Users.logout();
            }
        }
    };
});

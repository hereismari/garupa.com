
app.directive('navigationBar', function() {
    return {
        restrict: 'E',
        scope: {},
        templateUrl: '/app/directives/navigation-bar/template.html',
        css: '/app/directives/navigation-bar/style.css',

        controller: function($scope, $location, Users) {
            $scope.Users = Users;

            $scope.login = function(uid, passwd) {
                Users.login(uid, passwd).then(function(success) {
                    $location.path(success? '/perfil' : '/login');
                });
            };

            $scope.logout = function() {
                $location.path('/');
                Users.logout();
            };
        }
    };
});


app.directive('navigationBar', function() {
    return {
        restrict: 'E',
        scope: {},
        templateUrl: '/app/directives/navigation-bar/template.html',
        css: '/app/directives/navigation-bar/style.css',

        controller: function($scope, $translate, $state, $location, Users) {

            $scope.changeLanguage = function(key) {
                $translate.use(key);
            };

            $scope.Users = Users;
            $scope.form = new Object();

            $scope.showForm = function() {
                if($state.current.name == 'login') return false;
                return Users.logged == null;
            }

            $scope.login = function(form) {
                Users.login(form.uid, form.passwd).then(function(success) {
                    if(success) $location.path('/perfil');
                    else $state.go('login', { uid: form.uid });
                    form.uid = form.passwd = null;
                });
            };

            $scope.logout = function() {
                $location.path('/');
                Users.logout();
            };
        }
    };
});

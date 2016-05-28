
app.directive('userInfo', function() {
    return {
        restrict: 'E',
        scope: { user: '=', canEdit: '=' },
        templateUrl: '/app/directives/user-info/template.html',
        css: '/app/directives/user-info/style.css',

        controller: function($scope, $filter, Users) {

            function Row(name, data, placeholder, pattern) {
                this.name = name;
                this.data = data;
                this.placeholder = placeholder;
                this.pattern = pattern;
            }

            $scope.table = [
                new Row($filter('translate')('ENROLLMENT'), 'uid'),
                new Row($filter('translate')('NAME'),      'name',    'eg. Fulaninho da Silva',     '.{3,}'),
                new Row($filter('translate')('PHONE'),  'phone',   'eg. (83) 99988-1122',        '\\(\\d\\d\\) \\d{4,5}-\\d{4}'),
                new Row($filter('translate')('EMAIL'),    'email',   'eg. fulano.silva@email.com', '.+@.+\\..+')
            ];
        }
    };
});

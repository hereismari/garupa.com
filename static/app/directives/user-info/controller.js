
app.directive('userInfo', function() {
    return {
        restrict: 'E',
        scope: { user: '=' },
        templateUrl: '/app/directives/user-info/template.html',
        css: '/app/directives/user-info/style.css',

        controller: function($scope, Users) {
            $scope.canEdit = {
                value: $scope.user === Users.loggedUser
            };

            function Row(name, data, placeholder, pattern) {
                this.name = name;
                this.data = data;
                this.placeholder = placeholder;
                this.pattern = pattern;
            }

            $scope.table = [
                new Row('Matrícula', 'id'),
                new Row('Nome',      'name',    'ie.: Fulaninho da Silva',     '.{3,}'),
                new Row('Telefone',  'phone',   'ie.: (83) 99988-1122',        '\\(\\d\\d\\) \\d{4,5}-\\d{4}'),
                new Row('E-mail',     'email',   'ie.: fulano.silva@email.com', '.+@.+\\..+')
            ];
        }
    };
});

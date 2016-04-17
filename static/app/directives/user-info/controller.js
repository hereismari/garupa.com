
app.directive('userInfo', function() {
    return {
        restrict: 'E',
        scope: { user: '=', canEdit: '=' },
        templateUrl: '/app/directives/user-info/template.html',
        css: '/app/directives/user-info/style.css',

        controller: function($scope, Users) {

            function Row(name, data, placeholder, pattern) {
                this.name = name;
                this.data = data;
                this.placeholder = placeholder;
                this.pattern = pattern;
            }

            $scope.table = [
                new Row('Matrícula', 'uid'),
                new Row('Nome',      'name',    'eg. Fulaninho da Silva',     '.{3,}'),
                new Row('Telefone',  'phone',   'eg. (83) 99988-1122',        '\\(\\d\\d\\) \\d{4,5}-\\d{4}'),
                new Row('E-mail',    'email',   'eg. fulano.silva@email.com', '.+@.+\\..+')
            ];
        }
    };
});

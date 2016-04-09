
app.directive('userInfo', function() {
    return {
        restrict: 'E',
        scope: { user: '=' },
        templateUrl: '/app/user-info/user-info.html',
        css: '/app/user-info/user-info.css',

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

app.directive('userInfoRow', function() {
    return {
        restrict: 'A',
        scope: { row: '=userInfoRow', user: '=', canEdit: '=' },
        templateUrl: '/app/user-info/user-info-row.html',

        controller: function($scope, $element) {
            $scope.mode = 'view';

            $scope.submit = function() {
                $scope.user[$scope.row.data] = $scope.input;
                $scope.return();
            }

            $scope.edit = function() {
                $scope.mode = 'edit';
                $scope.canEdit.value = false;
                $scope.input = $scope.user[$scope.row.data];
                $element.addClass('selected');
            }

            $scope.return = function() {
                $scope.mode = 'view';
                $scope.canEdit.value = true;
                $element.removeClass('selected');
            }
        }
    };
});

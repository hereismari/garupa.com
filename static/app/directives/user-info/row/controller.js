
app.directive('userInfoRow', function() {
    return {
        restrict: 'A',
        scope: { row: '=userInfoRow', user: '=', canEdit: '=' },
        templateUrl: '/app/directives/user-info/row/template.html',

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

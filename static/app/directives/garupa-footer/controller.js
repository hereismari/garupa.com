app.directive('garupaFooter', function() {
    return {
        restrict: 'E',
        scope: {},
        templateUrl: '/app/directives/garupa-footer/template.html',
        css: '/app/directives/garupa-footer/style.css',

        controller: function($scope, $translate) {

            $scope.changeLanguage = function(key) {
                $translate.use(key);
                location.reload();
            };
        }
    };
});

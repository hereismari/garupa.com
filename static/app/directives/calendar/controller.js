
app.directive('calendar', function() {
    return {
        restrict: 'E',
        scope: { user: '=' },
        templateUrl: '/app/directives/calendar/template.html',
        css: '/app/directives/calendar/style.css',

        controller: function($scope, Day, Way) {
            $scope.Day = Day;
            $scope.Way = Way;
        }
    }
});

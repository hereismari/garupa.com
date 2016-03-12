
app.directive('calendar', function() {
    return {
        restrict: 'E',
        scope: { user: '=' },
        templateUrl: 'app/calendar/calendar.html',
        css: 'app/calendar/calendar.css',

        controller: function($scope, Day, Way) {
              $scope.Day = Day;
              $scope.Way = Way;
        }
    }
});

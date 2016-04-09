
app.directive('engrave', function() {
    return {
        restrict: 'A',
        transclude: true,
        scope: { engrave: '@' },
        template:
          "<i ng-class='icon'></i> &nbsp; <ng-transclude>",

        controller: function($scope) {
            $scope.icon = 'fa fa-' + $scope.engrave;
        }
    };
});

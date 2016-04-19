
app.controller('notifications', function($scope, $timeout) {

    $scope.notifications_list = [
        { status  : 1,
	  type    : "",
          date    : "dd/mm/aa",
          message : "message",
          user    : {},
        }
    ];

    $scope.delete = function(index) {
        $scope.notifications_list.splice(index, 1);
    }
});

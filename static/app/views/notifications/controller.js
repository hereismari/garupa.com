
app.controller('notifications', function($scope, $timeout) {

    $scope.ready = function() {
        $(' .pull-right ').click(function() {
            $(this).parent().css({'display': 'none'});
        });
    };

});

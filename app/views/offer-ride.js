
app.controller('offer-ride', function($scope, Day, Districts) {

    $("[name='origin']").bootstrapSwitch();

    $("[name='repeat']").bootstrapSwitch();

    $("[name='time']").timepicker();

    $("[name='tagsinput']").tagsinput();

    $("[name='calendar']").datepicker({
        format: "dd/mm/yyyy"
    });

    $scope.Day = Day;

    $scope.carpool = {
        from: 'Casa',
        to: 'UFCG',
        day: '',
        time: '',
        recurrent: false
    };

    $scope.dataSource = Districts;

    $("[name='repeat']").bootstrapSwitch('onSwitchChange', function(event, state) {
        $scope.carpool.recurrent = state;
        $scope.$apply();

        console.log(event)
    });

    $("[name='origin']").bootstrapSwitch('onSwitchChange', function(event, state) {
        $scope.carpool.from = state?  'UFCG' : 'Casa';
        $scope.$apply();

        console.log($scope.carpool.from)
    });
});

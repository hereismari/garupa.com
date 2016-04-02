
app.controller('offer-ride', function($scope, $timeout, Day, Districts) {

    $scope.Day = Day;
    $scope.Districts = Districts;

    $scope.carpool = {
        from: 'UFCG',
        day: undefined,
        time: undefined,
        route: undefined,
        recurrent: false
    };

    $scope.ready = function() {
        $('.calendar-input').datetimepicker({
            language: 'pt-BR',
            format: 'd M yyyy (h:ii)',
            fontAwesome: true,
            autoclose: true,
            startDate: new Date()
        });

        $('#origin').bootstrapSwitch('onSwitchChange', function(event, state) {
            $scope.carpool.from = state?  'UFCG' : 'Casa';
            $scope.$apply();
        });

        $('#repeat').bootstrapSwitch('onSwitchChange', function(event, state) {
            $scope.carpool.recurrent = state;
            $scope.$apply();
        });

        $('#route').select2({
            formatNoMatches: 'Nenhum bairro encontrado'
        });
    };
});

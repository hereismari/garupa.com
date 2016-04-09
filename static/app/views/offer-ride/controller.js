
app.controller('offer-ride', function($scope, $timeout, Day, Districts) {

    $scope.Day = Day;
    $scope.Districts = Districts;
    $scope.vacancies = _.range(1, 8, 1)

    $scope.carpool = {
        destination: 'UFCG',
        date: undefined,
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

        $('#destination').bootstrapSwitch('onSwitchChange', function(event, state) {
            $scope.carpool.destination = state?  'UFCG' : 'Casa';
            $scope.$apply();
        });

        $('#route').select2({
            formatNoMatches: 'Nenhum bairro encontrado'
        });
        
        $('#vacancies').select2({
            placeholder: 'Escolha um valor'
        });
    };
});

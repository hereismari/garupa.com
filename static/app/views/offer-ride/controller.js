
app.controller('offer-ride', function($scope, $location, Users, Districts, Destination) {

    $scope.Districts = Districts;
    $scope.seats = _.range(1, 8, 1)

    $scope.form = {
        dest: Destination.UFCG,
        repeat: false
    };

    $scope.submit = function() {
        Users.logged.registerRide($scope.form).then(function() {
            $location.path('/perfil');
        });
    };

    $scope.ready = function() {
        $('.calendar-input').datetimepicker({
            language: 'pt-BR', format: 'd M yyyy (h:ii)',
            fontAwesome: true, autoclose: true,
            startDate: new Date()
        })
            .on('changeDate', function(event) {
                $scope.form.date = event.date.getTime();
                $scope.$apply();
            });

        $('#destination').bootstrapSwitch('onSwitchChange', function(event, state) {
            $scope.form.dest = state?  Destination.UFCG : Destination.HOME;
            $scope.$apply();
        });

        $('#route').select2({
            formatNoMatches: 'Nenhum bairro encontrado'
        });

        $('#seats').select2({
            placeholder: 'Escolha um valor'
        });
    };
});


app.controller('offer-ride', function($scope, Day) {

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

    $scope.dataSource = [
        'Acacio Figueiredo', 'Alto Branco',
        'Bairro das Cidades', 'Bela Vista',
        'Bodocongo', 'Cachoeira',
        'Castelo Branco', 'Catole',
        'Catole de Ze Ferreira', 'Centenario',
        'Centro', 'Conjunto Cinza',
        'Dinamerica ', 'Distrito de Catole',
        'Distrito Industrial', 'Estacao Velha',
        'Estreito', 'Gloria', 'Itarare',
        'Jardim Atalaia', 'Jardim Borborema',
        'Jardim Paulistano', 'Jardim Verdejante',
        'Jeremias', 'Jose Pinheiro', 'Lauritzen',
        'Liberdade', 'Ligeiro', 'Louzeiro',
        'Malvinas', 'Mirante', 'Monte Castelo',
        'Monte Santo', 'Mutirao do Serrotao',
        'Nova Brasilia', 'Novo Bodocongo',
        'Palmeira', 'Pedregal', 'Prata',
        'Presidente Medici', 'Quarenta',
        'Ramadinha', 'Sandra Cavalcante',
        'Santa Cruz', 'Santa Rosa',
        'Santa Terezinha', 'Santo Antonio',
        'Sao Jose', 'Sao Jose da Mata',
        'Serrotao', 'Sitio Estreito', 'Sitio Lucas',
        'Tambor', 'Tres Irmas', 'Universitario',
        'Velame', 'Vila Cabral'
    ];

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

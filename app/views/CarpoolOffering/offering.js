
app.controller('offering', function($scope, Day) {

    $(document).ready(function() {
        $("[name='my-checkbox']").bootstrapSwitch();
    });

    $scope.Day = Day;

    $scope.carpool = {
        from: 'Casa',
        to: 'UFCG',
        day: '',
        time: ''
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

    $scope.$watch('carpool.from', function() {
        $scope.carpool.to = 'UFCG';
    });
});

$(document).ready(function () {

    //ativa o datepicker
    $('#date').datepicker({
        format: "dd/mm/yyyy"
    });

    //ativa o switch
    $("#way-cb").bootstrapSwitch();

    //ativa o timepicker
    $('#time').timepicker();
});

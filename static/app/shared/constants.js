
app.constant('Day', {
    SUN: {short: 'SUN', index: 0},
    MON: {short: 'MON', index: 1},
    TUE: {short: 'TUE', index: 2},
    WED: {short: 'WED', index: 3},
    THU: {short: 'THU', index: 4},
    FRI: {short: 'FRI', index: 5},
    SAT: {short: 'SAT', index: 6}
});

app.constant('NextWeek', (function() {
    var d = new Date();
    d.setHours(0, 0, 0, 0);
    d.setDate(d.getDate() - d.getDay() + 7);
    return d.getTime();
}()));

app.constant('Destination', {
    UFCG: 'UFCG',
    HOME: 'HOME'
});

app.constant('Districts', [
    'Acácio Figueiredo', 'Alto Branco', 'Bairro das Cidades', 'Bela Vista',
    'Bodocongó', 'Cachoeira', 'Castelo Branco', 'Catolé',
    'Catolé de Zé Ferreira', 'Centenário', 'Centro', 'Conjunto Cinza',
    'Dinamérica', 'Distrito de Catolé', 'Distrito Industrial', 'Estação Velha',
    'Estreito', 'Glória', 'Itararé', 'Jardim Atalaia', 'Jardim Borborema',
    'Jardim Paulistano', 'Jardim Verdejante', 'Jeremias', 'José Pinheiro',
    'Lauritzen', 'Liberdade', 'Ligeiro', 'Louzeiro', 'Malvinas', 'Mirante',
    'Monte Castelo', 'Monte Santo', 'Mutirão do Serrotão', 'Nova Brasília',
    'Novo Bodocongó', 'Palmeira', 'Pedregal', 'Prata', 'Presidente Médici',
    'Quarenta', 'Ramadinha', 'Sandra Cavalcante', 'Santa Cruz', 'Santa Rosa',
    'Santa Terezinha', 'Santo Antônio', 'São José', 'São José da Mata',
    'Serrotão', 'Sítio Estreito', 'Sítio Lucas', 'Tambor', 'Três Irmãs',
    'Universitário', 'Velame', 'Vila Cabral'
]);

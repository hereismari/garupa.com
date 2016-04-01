app.controller('search-rides', ['$scope', 'Users', 'Districts', function($scope, Users, Districts) {

    $scope.carpool = new Object();

    $scope.users = Users.getAll();
    $scope.filtered_rides = [];

    $scope.dataSource = Districts;

    $scope.searchWasMade = false;

    $scope.modal_title = "";
    $scope.modal_message = "";

    var ModalMessage = {
        SEND_INVITATION : { title: 'Enviar solicitacao de carona', message: 'O usuario sera notificado que voce quer essa carona!'},
        NOTIFY_ME : { title: 'Quero ser notificado', message: 'Voce sera notificado assim que uma carona desse tipo surgir!'},
        MAKE_A_FRIEND : { title: 'Solicitacao de amizade', message: 'O usuario sera notificado que voce quer ser seu amigo!'}
    };

    $scope.explanation_title = "Ache a carona perfeita para voce!";
    $scope.explanation = "Esta indo para UFCG ou voltando para casa e tem medo de ser assaltado se for andando ou entao dos outros males que nos cercam diariamente? Calma!!! Temos a carona perfeita para voce!";

    $scope.search = function() {

        $scope.filtered_rides = [];

        for(var i = 0; i < $scope.users.length; i++) {
            for(var j = 0; j < $scope.users[i].rides.length; j++) {
                var user = $scope.users[i];
                var ride = $scope.users[i].rides[j];
                if(ride.driver.address === $scope.address) {
                    $scope.filtered_rides.push(ride);
                    break;
                }
            }
        }

        $scope.searchWasMade = true;
    };

    $scope.setModalMessage = function(evt) {

        var id = evt.target.id;
        var modal_auxiliar = undefined;

        if(id == 'send-invitation') modal_auxiliar = ModalMessage.SEND_INVITATION;
        if(id == 'notify-me') modal_auxiliar = ModalMessage.NOTIFY_ME;
        if(id == 'make-a-friend') modal_auxiliar = ModalMessage.MAKE_A_FRIEND;

        $scope.modal_title = modal_auxiliar.title;
        $scope.modal_message = modal_auxiliar.message;

    }

    //ativa o switch
    $('#way-cb').bootstrapSwitch('onSwitchChange', function(event, state) {
        $scope.carpool.from = state?  'UFCG' : 'Casa';
        $scope.$apply();

        console.log($scope.carpool.from)
    });

    //ativa o datepicker
    $('#date').datepicker({
        format: "dd/mm/yyyy"
    });

}]);

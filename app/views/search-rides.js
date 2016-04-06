app.controller('search-rides', function($scope, Users, Districts) {

    $scope.Districts = Districts;
    $scope.search_result = null;

    $scope.carpool = {
        destination: 'UFCG',
        district: undefined,
        date: undefined,
        recurrent: false
    };

    var ModalMessage = {
        SEND_INVITATION : { title: 'Enviar solicitacao de carona', message: 'O usuario sera notificado que voce quer essa carona!'},
        NOTIFY_ME : { title: 'Quero ser notificado', message: 'Voce sera notificado assim que uma carona desse tipo surgir!'}
    };

    $scope.search = function() {
        $scope.search_result = Users.getAllRides();
    };

    $scope.setModalMessage = function(evt) {
        var id = evt.target.id;
        var modal_auxiliar = undefined;

        if(id == 'send-invitation') modal_auxiliar = ModalMessage.SEND_INVITATION;
        if(id == 'notify-me') modal_auxiliar = ModalMessage.NOTIFY_ME;

        $scope.modal_title = modal_auxiliar.title;
        $scope.modal_message = modal_auxiliar.message;
    };

    $scope.ready = function() {

        $('.calendar-input').datetimepicker({
            language: 'pt-BR',
            format: 'd MM yyyy (h:ii)',
            fontAwesome: true,
            autoclose: true,
            startDate: new Date()
        });

        $('#destination').bootstrapSwitch('onSwitchChange', function(event, state) {
            $scope.carpool.from = state?  'UFCG' : 'Casa';
            $scope.$apply();
        });

        $('#district').select2({
            placeholder: 'Bairro',
            formatNoMatches: 'Nenhum bairro encontrado',
            dropdownCssClass: 'show-select-search'
        });
    };

});

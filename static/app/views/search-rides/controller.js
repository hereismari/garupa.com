app.controller('search-rides', function($scope, Api, Users, Districts, Destination) {

    $scope.Districts = Districts;
    $scope.search_result = null;

    $scope.form = {
        dest: Destination.UFCG,
        repeat: false,
        page: 1
    };

    var ModalMessage = {
        SEND_INVITATION : { title: 'Enviar solicitacao de carona', message: 'O usuario sera notificado que voce quer essa carona!'},
        NOTIFY_ME : { title: 'Quero ser notificado', message: 'Voce sera notificado assim que uma carona desse tipo surgir!'}
    };

    $scope.search = function() {
        var form = $scope.form;
        Api.searchRides(form.dest, form.district, form.date, Users.logged.uid, form.page)
            .then(function(resp) {
                $scope.search_result = resp.data.result;
                $scope.pages = _.range(1, resp.data.pages+1);
            });
    };

    $scope.setPage = function(page) {
        $scope.form.page = page;
        $scope.search();
    };

    $scope.joinRide = function(ride) {
        Users.logged.joinRide(ride.rid).then(function() {
            alert('Bigu aceito!');
        });
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
            language: 'pt-BR', format: 'd MM yyyy (h:ii)',
            fontAwesome: true, autoclose: true,
            startDate: new Date()
        })
            .on('changeDate', function(event) {
                event.date.setSeconds(0, 0);
                $scope.form.date = event.date.getTime();
                $scope.$apply();
            });

        $('#destination').bootstrapSwitch('onSwitchChange', function(event, state) {
            $scope.form.dest = state?  Destination.UFCG : Destination.HOME;
            $scope.$apply();
        });

        $('#district').select2({
            placeholder: 'Bairro',
            formatNoMatches: 'Nenhum bairro encontrado',
            dropdownCssClass: 'show-select-search'
        });
    };

});

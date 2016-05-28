app.controller('search-rides', function($scope, $filter, Api, Users, Districts, Destination) {

    $scope.Districts = Districts;
    $scope.search_result = null;

    $scope.form = {
        dest: Destination.UFCG,
        weekly: false,
        page: 1
    };

    var ModalMessage = {
        SEND_INVITATION : { title: $filter('translate')('SEND_RIDE_REQUEST'), message: $filter('translate')('NOTIFY_USER') },
        NOTIFY_ME : { title: $filter('translate')('NOTIFY_ME'), message: $filter('translate')('YOU_WILL_BE_NOTIFIED') }
    };

    $scope.setPage = function(page) {
        $scope.form.page = page;
        $scope.search();
    };

    $scope.search = function() {
        var form = $scope.form;
        Api.searchRides(form.dest, form.district, form.date, form.weekly, form.page)
            .then(function(resp) {
                $scope.search_result = resp.data.results;
                $scope.pages = _.range(1, resp.data.pages+1);
            });
    };

    $scope.requestRide = function(ride) {
        var form = $scope.form;
        Api.requestRide(Users.logged.uid, ride.rid, form.district, form.complement)
            .then(function() {
                alert($filter('translate')('RIDE_REQUEST_SENT'));
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
            placeholder: $filter('translate')('DISTRICT'),
            formatNoMatches: $filter('translate')('NO_DISTRICT_FOUND'),
            dropdownCssClass: 'show-select-search'
        });
    };

});

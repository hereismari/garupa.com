
app.controller('notifications', function($scope, $state, $stateParams, Api, Users) {

    $scope.uid = Api.getCache().uid;

    // notifications types
    $scope.FRIEND_REQUEST  = "FRIEND_REQUEST";
    $scope.NEW_FRIEND      = "NEW_FRIEND";
    $scope.RIDE_FOUND      = "RIDE_FOUND";
    $scope.RIDE_REQUEST    = "RIDE_REQUEST";
    $scope.RIDE_ACCEPTED    = "RIDE_ACCEPTED";

    // notification status
    $scope.VIEWED = 0;

    // notification selected
    $scope.active = null;

    // notification actions
    $scope.filter = "$";
    $scope.search = "";

    // Notification list
    Api.get_notifications($scope.uid).then(
        function(resp) {
            $scope.notifications_list = resp.data;
        }
    );

    $scope.changeFilterTo = function(pr, attr) {
        $scope.filter = pr;
        $scope.search = attr;
    }

    $scope.getFilter = function() {
        if ($scope.filter == 'uid')
            return {uid: $scope.search};
        else if ($scope.filter == 'status')
            return {status: $scope.search};
        else if ($scope.filter == 'type')
            return {type: $scope.search};
        return {$: $scope.search};
    }

    $scope.getIndex = function (nid) {
        for (var index = 0; index < $scope.notifications_list.length; index++) {
            if (nid === $scope.notifications_list[index].nid)
                return index;
        }
        return null;
    }

    $scope.removeNotificationByIndex = function(index) {
        if (index != null) {
            $scope.notifications_list.splice(index, 1);
        }
    }

    $scope.hideNotification = function(nid) {
        var index = $scope.getIndex(nid);
        $scope.notifications_list[ index ].status = 0;
        $scope.removeNotificationByIndex( index );
    }

    $scope.markAsReadNotification = function(nid) {
        var index = $scope.getIndex(nid);
        var status = $scope.notifications_list[ index ].status;
        $scope.notifications_list[ index ].status = 1 - status;
    }

    $scope.acceptFriendRequest = function(uid, nid) {
        Users.logged.addFriend(uid);
        $scope.removeNotificationByIndex( $scope.getIndex(nid) );
        Users.logged.removeNotificationByID(nid);
    }

    $scope.acceptRideRequest = function(uid, ride, district, complement, nid) {
        Api.acceptRide(Users.logged.uid, uid, ride.rid, district, complement);
        $scope.removeNotificationByIndex( $scope.getIndex(nid) );
        Users.logged.removeNotificationByID(nid);
    }

    $scope.refuseRideRequest = function(nid) {
        $scope.removeNotificationByIndex( $scope.getIndex(nid) );
        Users.logged.removeNotificationByID(nid);
    }

    $scope.collapse = function(nid) {
        if ($scope.active != nid)
            $scope.active = nid;
        else
            $scope.active = null;
    };

    $scope.hoverIn = function() {
        this.removable = true;
    }

    $scope.hoverOut = function() {
        this.removable = false;
    }
});


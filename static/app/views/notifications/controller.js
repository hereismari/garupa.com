
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

    $scope.getIndex = function (uid) {
        for (var index = 0; index < $scope.notifications_list.length; index++) {
            if (uid === $scope.notifications_list[index].associatedUser.uid)
                return index;
        }
        return null;
    }

    $scope.removeNotificationByIndex = function(index) {
        if (index != null) {
            $scope.notifications_list.splice(index, 1);
        }
    }

    $scope.hideNotification = function(uid) {
        var index = $scope.getIndex(uid);
        $scope.notifications_list[ index ].status = 0;
        $scope.removeNotificationByIndex( index );
    }

    $scope.markAsReadNotification = function(uid) {
        var index = $scope.getIndex(uid);
        var status = $scope.notifications_list[ index ].status;
        $scope.notifications_list[ index ].status = 1 - status;
    }

    $scope.acceptFriendRequest = function(uid) {
        Users.logged.addFriend(uid);
        $scope.removeNotificationByIndex( $scope.getIndex(uid) );
        //Users.logged.removeNotification(notification);
    }

    $scope.acceptRideRequest = function(uid, ride, district, complement) {
        Api.acceptRide(Users.logged.uid, uid, ride.rid, district, complement);
        $scope.removeNotificationByIndex( $scope.getIndex(uid) );
        //Users.logged.removeNotification(notification);
    }

    $scope.refuseRideRequest = function(uid) {
        $scope.removeNotificationByIndex( $scope.getIndex(uid) );
        //Users.logged.removeNotification(notification);
    }

    $scope.collapse = function(uid) {
        if ($scope.active != uid)
            $scope.active = uid;
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

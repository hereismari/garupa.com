
app.controller('notifications', function($scope, Api, Users) {

    var uid = Api.getCache().uid;
    var notifications = undefined;

    function sync() {
        return Api.getNotifications(uid).then(function(resp) {
            notifications = resp.data;
        });
    }

    $scope.filter = {
        seen: false,
        type: undefined
    };

    function applyFilter(notification) {
        if(notification.seen != $scope.filter.seen)
            return false;

        var mode = {
            'FRIEND': ['FRIEND_REQUEST', 'NEW_FRIEND'],
            'RIDE': ['RIDE_REQUEST', 'RIDE_ACCEPTED']
        };

        if($scope.filter.type != undefined)
            if(_.contains(mode[$scope.filter.type], notification.type) == false)
                return false;

        return true;
    }

    $scope.filtered = function() {
        var list = _.filter(notifications, applyFilter);

        return _.sortBy(list, function(notification) {
            return -notification.timestamp;
        });
    };

    $scope.remove = function(notification) {
		Users.logged.removeNotification(notification.nid).then(sync);
    };

    $scope.archive = function(notification) {
        Users.logged.markNotification(notification.nid).then(sync);
    };

    $scope.acceptFriend = function(notification) {
        Users.logged.addFriend(notification.data.user.uid);
        $scope.archive(notification);
    };

    $scope.acceptRide = function(notification) {
        Users.logged.acceptRide(
            notification.data.user.uid, notification.data.ride.rid,
            notification.data.district, notification.data.complement);
        $scope.archive(notification);
    };

    sync();
});

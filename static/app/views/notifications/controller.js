
app.controller('notifications', function($scope, $state, $stateParams, Api, Users) {

    //$scope.uid = Api.getCache().uid;

    // notifications types
    $scope.FRIEND_REQUEST  = 1;
    $scope.NEW_FRIEND      = 2;
    $scope.RIDE_FOUND      = 3;
    $scope.RIDE_REQUEST    = 4;

    // notification status
    $scope.VIEWED = 0;

    // Notification list
    /*
    Api.get_notifications($scope.uid)
    .then(function(resp) {
            $scope.notifications_list = resp.data;
    });
    */

    // user abstraction is the same on the server side
    function User(uid) {
        this.uid = uid;
        this.password = null;
        this.name = null;
        this.email = null;
        this.phone = undefined;
        this.photo = undefined;
        this.rides = new Array();
    }

    // fake rides
    function Ride() {
        this.driver = null;
        this.numberOfVacancies = 0;
        this.date = undefined;

        self.weekly = false;
        self.toUFCG = false;

        this.passengers = new Array();
        this.routes = new Array();

        this.associatedUser = null;
    }

    // fake users
    var user1 = new User('dilmae');
    user1.name = "Dilma Rousseff";
    user1.photo = "//40.media.tumblr.com/20625bfafa453b4d628f7de4a5d7e14e/tumblr_nz7u21Qai41t4osjeo2_250.png";
    var ride1 = new Ride();
    ride1.driver = "Fulano";
    ride1.numberOfVacancies = 2;
    ride1.date = "25 de abr às 12:15";
    ride1.weekly = false;
    ride1.toUFCG = true;
    ride1.routes.push("Alto Branco");
    ride1.passengers.push(new User("cicrano"));
    ride1.passengers.push(new User("deutrano"));

    user1.rides.push(ride1);

    var user2 = new User('einsten');
    user2.name = "Albert Einsten";
    user2.photo = "https://pbs.twimg.com/profile_images/435830531951837184/Z50DeEtx.jpeg";

    var user3 = new User('temer');
    user3.name = "Temer babadi";
    user3.photo = "http://blogdomarioflavio.com.br/vs1/wp-content/uploads/2016/01/Michel-Temer-foto-Ag%C3%AAncia-Brasil-150x150.jpg";

    var ride2 = new Ride();
    ride2.date = "25 de abr às 12:15";
    ride2.routes.push("Alto Branco");

    user3.rides.push(ride2);

    var user4 = new User('billy');
    user4.name = "Billy the Kid";
    user4.photo = "https://upload.wikimedia.org/wikipedia/en/thumb/7/79/Brushy_Bill_Roberts.jpg/220px-Brushy_Bill_Roberts.jpg";
    // notification actions
    $scope.filter = "$";
    $scope.search = "";

    // notification selected
    $scope.active = null;

    $scope.notifications_list = [
        { status         : 1,
          type           : 1,
          date           : "21 de abr",
          message        : "enviou uma solicitação de amizade",
          ride           : "",
          associatedUser : user2
        },

        { status         : 1,
          type           : 2,
          date           : "21 de abr",
          message        : "aceitou seu pedido de amizade",
          ride           : "20 de abr",
          associatedUser : user4
        },

        { status         : 1,
          type           : 3,
          date           : "26 de mai",
          message        : "Uma carona surgiu.",
          ride           : "UFCG",
          associatedUser : user1
        },

        { status         : 1,
          type           : 4,
          date           : "19 de abr",
          message        : "quer participar de uma carona",
          ride           : "",
          associatedUser : user3
        }
    ];

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
        $scope.removeNotificationByIndex( $scope.getIndex(uid) );
        //Users.addFriend(uid);
    }

    $scope.acceptRideRequest = function(uid) {
        $scope.removeNotificationByIndex( $scope.getIndex(uid) );
        // send notification to uid
        // add <uid> to rides
        //Users.registerRide(uid);
    }

    $scope.refuseRideRequest = function(uid) {
        $scope.removeNotificationByIndex( $scope.getIndex(uid) );
        // send notification to uid
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



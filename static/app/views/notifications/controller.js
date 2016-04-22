
app.controller('notifications', function($scope, $timeout) {

    var removable = false;
    var displayInfo = false;

    // notifications types
    $scope.FRIEND_REQUEST  = 1;
    $scope.NEW_FRIEND      = 2;
    $scope.RIDE_FOUND      = 3;
    $scope.RIDE_REQUEST    = 4;

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
    ride1.date = "25 de abr";
    ride1.weekly = false;
    ride1.toUFCG = true;
    ride1.passengers.push(new User("cicrano"));
    ride1.passengers.push(new User("deutrano"));

    user1.rides.push(ride1);

    var user2 = new User('einsten');
    user2.name = "Albert Einsten";
    user2.photo = "https://pbs.twimg.com/profile_images/435830531951837184/Z50DeEtx.jpeg";

    var user3 = new User('einsten2.0');
    user3.name = "Albert Einsten";
    user3.photo = "https://pbs.twimg.com/profile_images/435830531951837184/Z50DeEtx.jpeg";


    $scope.notifications_list = [
        { status         : 1,
          type           : 1,
          date           : "21 de abr",
          message        : "enviou uma solicitação de amizade",
          ride           : "",
          associatedUser : user1
        },

        { status         : 0,
          type           : 2,
          date           : "21 de abr",
          message        : "aceitou seu pedido de amizade",
          ride           : "20 de abr",
          associatedUser : user2
        },

        { status         : 1,
          type           : 4,
          date           : "19 de abr",
          message        : "quer participar da carona do dia 25/04/2016",
          ride           : "",
          associatedUser : user1
        },

        { status         : 0,
          type           : 3,
          date           : "26 de mai",
          message        : "Uma carona surgiu.",
          ride           : "",
          associatedUser : user1
        }
    ];
    
    // Notification actions
    
    $scope.acceptFriendRequest = function(index, uid) {
        $scope.notifications_list.splice(index, 1);
        // add <uid> to friends
    }

    $scope.showInfo = function() {
        $scope.displayInfo = !$scope.displayInfo; 
    }

    $scope.delete = function(index) {
        $scope.notifications_list.splice(index, 1);
    }    

    $scope.hoverIn = function() {
        this.removable = true;
    }

    $scope.hoverOut = function() {
        this.removable = false;
    }
});
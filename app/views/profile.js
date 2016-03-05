
app.controller('profile', function($scope, $stateParams, Day, Way) {

    function Ride(time, day, way, driver) {
        this.time = time;
        this.day = day;
        this.driver = driver;
        this.way = way;
    }

    function User(id) {
        var self = this;

        this.id = id;
        this.email = null;
        this.password = null;

        this.name = undefined;
        this.phone = undefined;
        this.address = undefined;
        this.photo_url = 'https://lh3.googleusercontent.com/-yysr8_T4r7k/AAAAAAAAAAI/AAAAAAAAAAA/EnhQ3HVLDok/photo.jpg';

        this.rides = new Array();
        this.friends = new Array();

        this.addRide = function(time, day, way, driver) {
            self.rides.push(new Ride(time, day, way, driver));
        }

        this.addFriend = function(user) {
            self.friends.push(user);
        }

        this.removeFriend = function(user) {
            self.friends = _.without(self.friends, user);
        }

        this.isFriendsWith = function(user) {
            return _.contains(self.friends, user)
                && _.contains(user.friends, self)
        }
    };

    // Fake users

    var user1 = new User('dilma');
    var user2 = new User('einstein');
    var user3 = new User('safadao');

    var user_list = [
        user1, user2, user3
    ];

    user1.addFriend(user2);
    user1.addFriend(user3);
    user2.addFriend(user1);
    user2.addFriend(user3);
    user3.addFriend(user1);

    user1.name = 'Dilma Rousseff';
    user2.name = 'Albert Einstein';
    user3.name = 'Wesley Safadão';

    user1.email = 'dilmona@presidente.br';
    user1.phone = '33331122';
    user1.address = 'Casa Branca';
    user1.photo_url = 'http://economia.estadao.com.br/blogs/joao-villaverde/wp-content/uploads/sites/44/2015/08/Dilma-1.jpg';

    user1.addRide(1000, Day.SUN, Way.FROM, user2);
    user1.addRide(730, Day.SUN, Way.TO, user1);
    user1.addRide(800, Day.MON, Way.TO, user2);
    user1.addRide(800, Day.TUE, Way.FROM, user3);
    user1.addRide(1130, Day.THU, Way.TO, user1);
    user1.addRide(730, Day.THU, Way.FROM, user2);
    user1.addRide(730, Day.SAT, Way.TO, user3);
    user1.addRide(1300, Day.SUN, Way.FROM, user2);
    user1.addRide(500, Day.SUN, Way.TO, user1);

    user2.addRide(500, Day.TUE, Way.TO, user1);

    // End fake users

    $scope.logged_user = user1;
    $scope.user = _.find(user_list, function(user) {
        return user.id === $stateParams.user_id;
    });

    $scope.signed = $scope.user === $scope.logged_user;
    $scope.visible = $scope.user.isFriendsWith($scope.logged_user);

    $scope.table = _.map([
        ['Nome',      $scope.user.name   ],
        ['Telefone',  $scope.user.phone  ],
        ['Endereço',  $scope.user.address],
        ['Matrícula', $scope.user.id     ],
        ['Email',     $scope.user.email  ],
        ['Senha',     '**********'       ]
    ],
        function(row) {
            return { name: row[0], data:row[1] };
        });
});

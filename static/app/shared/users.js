
app.service('Users', function($q, Api, Cookie) {
    var self = this;

    function Ride(time, day, way, driver, seats, recurrent) {
        this.time = time;
        this.day = day;
        this.driver = driver;
        this.way = way;
        this.seats = seats;
        this.recurrent = recurrent;
    }

    function User() {
        var self = this;

        this.uid = null;
        this.password = null;

        this.name = null;
        this.email = null;

        this.phone = undefined;
        this.photo = undefined;

        this.rides = new Array();

        this.sync = function() {
            return Api.viewUser(self.uid).then(function(resp) {
                _.extend(self, resp.data);
            });
        };

        this.addFriend = function(uid) {
            return Api.addFriend(self.uid, uid);
        };

        this.removeFriend = function(uid) {
            return Api.removeFriend(self.uid, uid);
        };

        this.update = function(attr, value) {
            return Api.updateUser(self.uid, attr, value).then(self.sync);
        };

        this.registerRide = function(ride) {
            ride = _.clone(ride); ride.driver = self.uid;
            return Api.registerRide(ride).then(self.sync);
        };
    }

    /*// Fake users

    var user1 = new User('dilma', 'votempt');
    var user2 = new User('einstein', 'loacepeso');
    var user3 = new User('safadao', 'soasnovinhas');

    var user_list = [
        user1, user2, user3
    ];

    user1.name = 'Dilma Rousseff';
    user2.name = 'Albert Einstein';
    user3.name = 'Wesley Safadão';

    user1.email = 'dilmona@presidente.br';
    user2.email = 'albert@ciencia.e.mc2';
    user3.email = 'garota@safada.voce';

    user1.phone = '(13) 1313-1313';
    user2.phone = '(18) 6736-2672';
    user3.phone = '(82) 9372-4408';

    user1.photo_url = 'http://static2.blastingnews.com/media/photogallery/2016/2/23/290x290/b_290x290/salario-de-dilma-devera-ser-reduzido_615715.jpg';
    user2.photo_url = 'https://pbs.twimg.com/profile_images/435830531951837184/Z50DeEtx.jpeg';
    user3.photo_url = 'https://40.media.tumblr.com/20625bfafa453b4d628f7de4a5d7e14e/tumblr_nz7u21Qai41t4osjeo2_250.png';

    user1.addRide(1000, Day.SUN, Way.FROM, user2, 3, false);
    user1.addRide(730, Day.SUN, Way.TO, user1, 2, true);
    user1.addRide(800, Day.MON, Way.TO, user2, 4, true);
    user1.addRide(800, Day.TUE, Way.FROM, user3, 5, false);
    user1.addRide(1130, Day.THU, Way.TO, user1, 1, false);
    user1.addRide(730, Day.THU, Way.FROM, user2, 0, true);
    user1.addRide(730, Day.SAT, Way.TO, user3, 1, false);
    user1.addRide(1300, Day.SUN, Way.FROM, user2, 4, true);
    user1.addRide(500, Day.SUN, Way.TO, user1, 5, true);

    user2.addRide(500, Day.TUE, Way.TO, user1, 2, true);

    // End fake users*/

    this.cacheUID = new Cookie('garupa.uid');

    this.get = function(uid, vuid) {
        return $q(function(resolve, reject) {
            if(self.logged && uid == self.logged.uid)
                return resolve(self.logged);

            Api.viewUser(uid, vuid).then(
                function(resp) {
                    var user = new User();
                    _.extend(user, resp.data);
                    resolve(user);
                },

                function(resp) {
                    if(resp.status == 404) resolve(null);
                    else reject(resp);
                });
        });
    };

    this.login = function(uid) {
        return self.get(uid).then(
            function(user) {
                if(user == null) {
                    self.logged = null;
                    self.cacheUID.erase();
                    return false;
                }

                self.logged = user;
                self.cacheUID.set(uid);
                return true;
            });
    };

    this.logout = function() {
        self.logged = null;
        self.cacheUID.erase();
    };

    var uid = this.cacheUID.get();
    if(uid != null) this.login(uid);
});

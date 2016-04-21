
app.service('Users', function($q, Api, Cookie) {
    var self = this;

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

        this.joinRide = function(rid, district, complement) {
            return Api.joinRide(self.uid, rid, district, complement).then(self.sync);
        };

        this.cancelRide = function(rid) {
            return Api.cancelRide(self.uid, rid).then(self.sync);
        };
    }

    this.get = function(uid) {
        return $q(function(resolve, reject) {
            if(self.logged && uid == self.logged.uid)
                return resolve(self.logged);

            Api.viewUser(uid).then(
                function(resp) {
                    var user = new User();
                    _.extend(user, resp.data);
                    resolve(user);
                },

                function(resp) {
                    resolve(null);
                });
        });
    };

    this.login = function(uid, passwd) {
        if(uid == null) uid = Api.getCache().uid;
        else Api.setCache(uid, passwd);

        return self.get(uid).then(function(user) {
            if(user == null) {
                self.logout();
                return false;
            }

            self.logged = user;
            return true;
        });
    };

    this.logout = function() {
        self.logged = null;
        Api.clearCache();
    };

    if(Api.getCache().uid != null)
    this.login().then(function(success) {
        if(success == false) location.reload();
    });
});

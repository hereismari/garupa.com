
app.service('Users', function($q, Api, Cookie) {
    var self = this;

    this.cacheUID = new Cookie('garupa.uid');

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
        vuid = self.cacheUID.get();

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
    if(uid != null) this.login(uid).then(function(success) {
        if(success == false) location.reload();
    });
});

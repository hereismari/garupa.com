
app.service('Api', function($http) {

    this.registerUser = function(user) {
        return $http({
            method: 'POST',
            url: '/api/users',
            data: user
        });
    };

    this.viewUser = function(uid, vuid) {
        return $http({
            method: 'GET',
            url: '/api/users/' + uid,
            params: {vuid: vuid}
        });
    };

    this.updateUser = function(uid, attr, value) {
        return $http({
            method: 'PUT',
            url: '/api/users/' + uid + '/' + attr,
            data: value
        });
    };

    this.addFriend = function(uid, fuid) {
        return $http({
            method: 'POST',
            url: '/api/users/' + uid + '/friends',
            data: fuid
        });
    };

    this.removeFriend = function(uid, fuid) {
        return $http({
            method: 'DELETE',
            url: '/api/users/' + uid + '/friends/' + fuid
        });
    };

    this.registerRide = function(ride) {
        return $http({
            method: 'POST',
            url: '/api/rides',
            data: ride
        });
    };

    this.joinRide = function(uid, rid, district, complement) {
        return $http({
            method: 'POST',
            url: '/api/users/' + uid + '/rides',
            data: {
                rid: rid,
                district: district,
                complement: complement
            }
        });
    };

    this.cancelRide = function(uid, rid) {
        return $http({
            method: 'DELETE',
            url: '/api/users/' + uid + '/rides/' + rid
        });
    };

    this.searchRides = function(dest, district, date, weekly, uid, page, limit) {
        return $http({
            method: 'GET',
            url: '/api/rides',
            params: {
                dest: dest, district: district,
                date: date, weekly: weekly, uid:  uid,
                page: page, limit: limit
            }
        });
    };

});

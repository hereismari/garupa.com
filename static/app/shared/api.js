
app.service('Api', function($http) {

    // args = name, uid, email, passwd
    this.register = function(args) {
        return $http({
            method: 'POST',
            url: '/api/user/register',
            data: args
        });
    };

    // args = uid, [vid]
    this.userView = function(uid, vid) {
        return $http({
            method: 'GET',
            url: '/api/user/' + uid,
            params: {'vid': vid}
        });
    };

    // args = [name], [email], [phone], [photo_url]
    this.updateUser = function(uid, attr, value) {
        return $http({
            method: 'POST',
            url: '/api/user/' + uid,
            data: [attr, value]
        });
    };
});


app.service('Api', function($http) {

    // args = name, uid, email, passwd
    this.register = function(args) {
        return $http({
            method: 'POST',
            url: '/api/register',
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
});

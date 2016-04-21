
app.factory('Cookie', function($cookies) {
    return function(name) {
        var self = this;
        this.name = name;

        this.get = function() {
            return $cookies.get(self.name);
        };

        this.set = function(value) {
            $cookies.put(self.name, value);
        };

        this.erase = function() {
            $cookies.remove(self.name);
        };
    };
});

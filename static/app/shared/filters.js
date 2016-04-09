
app.filter('time', function() {
    return function(input) {
        return Math.floor(input/100) + ':' + ('0' + input%100).slice(-2);
    }
})

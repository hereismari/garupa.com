
var app = angular.module("app", [
  "ngAnimate", "ui.router", "door3.css"
]);

app.config(function($stateProvider, $cssProvider) {
    $stateProvider
        .state('search-rides', {
            url: '/',
            controller: 'search-rides',
            templateUrl: 'app/views/search-rides/search-rides.html'
        });
    
    angular.extend($cssProvider.defaults, {
        persist: true,
        preload: true
    });
});

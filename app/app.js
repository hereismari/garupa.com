
var app = angular.module("app", [
    "ngAnimate", "ui.router", "door3.css",
]);

app.config(function($stateProvider, $cssProvider) {
    $stateProvider
        .state('offering', {
            url: '/',
            controller: 'offering',
            templateUrl: 'app/views/CarpoolOffering/offering.html',
            css: 'app/views/CarpoolOffering/offering.css'
        });
    
    angular.extend($cssProvider.defaults, {
        persist: true,
        preload: true
    });
});


var app = angular.module('app', [
  'ngAnimate', 'ui.router', 'door3.css'
]);

app.config(function($stateProvider, $urlRouterProvider, $locationProvider, $cssProvider) {
    //$locationProvider.html5Mode(true);
    $urlRouterProvider.otherwise('/perfil/dilma');

    $stateProvider
        .state('profile', {
            url: '/perfil/{user_id}',
            controller: 'profile',
            templateUrl: 'app/views/profile.html',
            css: 'app/views/profile.css'
        });

    angular.extend($cssProvider.defaults, {
        persist: true
    });
});


var app = angular.module('app', [
  'ngAnimate', 'ui.router', 'door3.css'
]);

app.config(function($stateProvider, $urlRouterProvider, $locationProvider, $cssProvider) {
    //$locationProvider.html5Mode(true);

    $urlRouterProvider
        .when('', '/perfil')

        .when('/perfil', function($state, Users) {
            return '/perfil/' + Users.loggedUser.id;
        })

        .when('/perfil/:uid', function($state, $match, Users) {
            var user = Users.get($match.uid);
            if(user == null) return false;

            $state.go(Users.areFriends(user, Users.loggedUser) || user === Users.loggedUser?
                'profile' : 'add-friend', { uid: user.id });
            })

        .otherwise('/404');

    $stateProvider
        .state('profile', {
            controller: 'profile',
            templateUrl: 'app/views/profile.html',
            css: 'app/views/profile.css',
            params: { uid: null }
        })

        .state('add-friend', {
            controller: 'add-friend',
            templateUrl: 'app/views/add-friend.html',
            params: { uid: null }
        })

        .state('404', {
            url: '/404',
            template: 'Not Found 404',
        });

    angular.extend($cssProvider.defaults, {
        persist: true,
        preload: true
    });
});

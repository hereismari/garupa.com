
var app = angular.module('app', [
  'ngAnimate', 'ui.router', 'door3.css'
]);

app.config(function($stateProvider, $urlRouterProvider, $locationProvider, $cssProvider) {
    //$locationProvider.html5Mode(true);

    $urlRouterProvider
        .when('', '/perfil')

        .when('/perfil', function($state, Users) {
            $state.go('profile', {
                uid: Users.loggedUser.id
            });
        })

        .when('/perfil/:uid', function($state, $match, Users) {
            var user = Users.get($match.uid);
            if(Users.areFriends(user, Users.loggedUser) || user === Users.loggedUser)
              return false;

            $state.go('add-friend', {
                uid: user.id
            });
        })

        .otherwise('/404');

    $stateProvider
        .state('profile', {
            url: '/perfil/:uid',
            controller: 'profile',
            templateUrl: 'app/views/profile.html',
            css: 'app/views/profile.css'
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
        persist: true
    });
});

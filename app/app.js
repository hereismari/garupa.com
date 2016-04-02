
var app = angular.module('app', [
    'ui.router', 'door3.css'
]);

app.config(function($stateProvider, $urlRouterProvider, $locationProvider, $cssProvider) {
    //$locationProvider.html5Mode(true);

    $urlRouterProvider
        .when('', '/')

        .when(/login|recuperar-senha/, function($state, $match, Users) {
            return Users.loggedUser != null? '/perfil':
                $state.go($match == 'recuperar-senha'? 'recover' : 'login');
        })

        .when(/\/.+/, function($state, $location, Users) {
            return Users.loggedUser != null? false:
                $state.go('login', { redirect: $location.url() });
        })

        .when('/perfil', function($state, Users) {
            return '/perfil/' + Users.loggedUser.id;
        })

        .when('/perfil/:uid', function($state, $location, $match, Users) {
            var user = Users.get($match.uid);
            if(user == null) return $state.go('404');

            $state.go(Users.areFriends(user, Users.loggedUser) || user === Users.loggedUser?
                'profile' : 'add-friend', { uid: user.id });
            })

        .otherwise(function($injector) {
            $injector.get('$state').go('404')
        });

    $stateProvider
        .state('home', {
            url: '/',
            controller: 'home',
            templateUrl: 'app/views/home.html',
            css: 'app/views/home.css'
        })

        .state('login', {
            url: '/login',
            controller: 'login',
            templateUrl: 'app/views/login.html',
            params: { redirect: '/perfil' }
        })

        .state('recover', {
            url: '/recuperar-senha',
            controller: 'recover',
            templateUrl: 'app/views/recover.html'
        })

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

        .state('search-rides', {
            url: '/procurar-bigu',
            controller: 'search-rides',
            templateUrl: 'app/views/search-rides.html',
            css: 'app/views/search-rides.css'
        })

        .state('offer-ride', {
            url: '/oferecer-bigu',
            controller: 'offer-ride',
            templateUrl: 'app/views/offer-ride.html'
        })

        .state('notifications', {
			url: '/notificacoes',
			templateUrl: 'app/views/notifications.html',
			css: 'app/views/notifications.css'
		})

        .state('404', {
            templateUrl: 'app/views/not-found.html',
            css: 'app/views/not-found.css',
        });

    angular.extend($cssProvider.defaults, {
        persist: true,
        preload: true
    });
});

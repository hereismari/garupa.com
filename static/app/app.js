
var app = angular.module('app', [
    'ui.router', 'door3.css', 'ngCookies', 'angular-loading-bar'
]);

app.config(function($stateProvider, $urlRouterProvider, $locationProvider, $cssProvider) {
    $locationProvider.html5Mode(true);

    $urlRouterProvider
        .when('', '/')

        .when(/login|recuperar-senha/, function($state, $match, Api) {
            return Api.getCache().uid != null? '/perfil':
                $state.go($match == 'recuperar-senha'? 'recover' : 'login');
        })

        .when(/\/.+/, function($state, $location, Api) {
            return Api.getCache().uid != null? false:
                $state.go('login', { redirect: $location.url() });
        })

        .when('/perfil', function($state, Api) {
            return '/perfil/' + Api.getCache().uid;
        })

        .when('/perfil/:uid', function($state, $location, $match, Users) {
            return Users.get($match.uid).then(function(user) {
                if(user == null) $state.go('404');
                else $state.go(/self|friend/.test(user.relationship)?
                    'profile' : 'add-friend', { uid: user.uid });
            });
        })

        .otherwise(function($injector) {
            $injector.get('$state').go('404')
        });

    $stateProvider
        .state('home', {
            url: '/',
            controller: 'home',
            templateUrl: '/app/views/home/template.html'
        })

        .state('login', {
            url: '/login',
            controller: 'login',
            templateUrl: '/app/views/login/template.html',
            params: { redirect: '/perfil', uid: null }
        })

        .state('recover', {
            url: '/recuperar-senha',
            controller: 'recover',
            templateUrl: '/app/views/recover/template.html'
        })

        .state('profile', {
            controller: 'profile',
            templateUrl: '/app/views/profile/template.html',
            css: '/app/views/profile/style.css',
            params: { uid: null }
        })

        .state('add-friend', {
            controller: 'add-friend',
            templateUrl: '/app/views/add-friend/template.html',
            params: { uid: null }
        })

        .state('search-rides', {
            url: '/procurar-bigu',
            controller: 'search-rides',
            templateUrl: '/app/views/search-rides/template.html'
        })

        .state('offer-ride', {
            url: '/oferecer-bigu',
            controller: 'offer-ride',
            templateUrl: '/app/views/offer-ride/template.html'
        })

        .state('notifications', {
			url: '/notificacoes',
			templateUrl: '/app/views/notifications/template.html',
			css: '/app/views/notifications/style.css'
		})

        .state('404', {
            templateUrl: '/app/views/not-found/template.html',
            css: '/app/views/not-found/style.css',
        });

    angular.extend($cssProvider.defaults, {
        persist: true,
        preload: true
    });
});

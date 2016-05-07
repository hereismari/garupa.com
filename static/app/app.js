var app = angular.module('app', [
    'ui.router', 'door3.css', 'ngCookies', 'angular-loading-bar', 'pascalprecht.translate'
]);

var translationsEN = {
    
    BUTTON_LANG_EN: 'english',
    BUTTON_LANG_PT: 'portuguese',
    
    HELLO: 'Welcome to Garupa.com!',
    HOME_DESCRIPTION: 'Offer rides or search for rides to UFCG and make new friends!',

    SIGN-UP: 'Sign-up'
};

var translationsPT = {
    
    BUTTON_LANG_EN: 'inglês',
    BUTTON_LANG_PT: 'português',
    
    HELLO: 'Bem-vindo ao Garupa.com!',
    HOME_DESCRIPTION: 'Consiga ou ofereça carona para a Universidade e faça novas amizades!',

    SIGN-UP: 'Cadastre-se'

};

app.config(function($stateProvider, $urlRouterProvider, $locationProvider, $cssProvider, $translateProvider) {

    $translateProvider.translations('en', translationsEN);
    $translateProvider.translations('pt', translationsPT);
   
    $translateProvider.preferredLanguage('pt');
    $translateProvider.fallbackLanguage('pt');

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
            templateUrl: '/app/views/recover/template.html',
            params: { uid: null }
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
            controller: 'notifications',
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

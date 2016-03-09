'use strict';

var app = angular.module('app', ['ngRoute']);

app.config(function($routeProvider) {

    $routeProvider
        .when('/', {
            templateUrl: 'app/views/home.html',
            controller: 'homeController',    
        })
        .when('/login', {
            templateUrl: 'app/views/login.html',
            controller: 'loginController'
        })
        .when('/recover', {
            templateUrl: 'app/views/recover.html',
            controller: 'recoverController'
        })
        .otherwise({ redirectTo: '/'});
});
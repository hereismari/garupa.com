'use strict';

var app = angular.module('app', ['ngRoute']);

app.config(function($routeProvider) {

    $routeProvider
        .when('/', {
            controller: 'homeController',    
            templateUrl: 'app/views/home.html',
            css: 'app/styles/home.css'
        })
        .otherwise({ redirectTo: '/'});
});
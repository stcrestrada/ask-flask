(function () {
    'use strict';

    var app = angular.module('askFlaskApp', [
        'ui.router',
        'ngCookies'
    ]);

    app.config(function ($stateProvider, $urlRouterProvider) {
        $urlRouterProvider.otherwise('/login');
        $stateProvider
            .state('/login',
                {
                    url: '/login',
                    templateUrl: 'app/login/login.html',
                    controller: 'LoginCtrl'
                })
            .state('instances',
                {
                    url: '/instances',
                    templateUrl: 'app/instance/instance.html',
                    controller: 'InstanceCtrl'
                })
    })
})();
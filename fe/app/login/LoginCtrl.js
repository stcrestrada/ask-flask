/**
 * Created by stephenestrada on 5/22/17.
 */
(function () {
    'use strict';

    angular.module('askFlaskApp')
        .controller('LoginCtrl', ['$state', '$scope', 'LoginService', function ($state, $scope, LoginService) {
            $scope.login = function () {
                var accessKey = $scope.accessKey;
                var secretKey = $scope.secretKey;

                LoginService.login(accessKey, secretKey)
                    .then(function (result) {
                        if(result.status === 200) {
                            $state.go('instances')
                        }
                    })


            }

        }])
})();
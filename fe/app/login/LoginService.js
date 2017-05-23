(function () {
    'use strict';

    angular.module('askFlaskApp')
        .factory('LoginService', [
            "$http", "$q", "UrlService", "$window", "$cookies", function ($http, $q, UrlService, $window) {

                function login(accessKey, secretKey) {
                    var userInfo;
                    var deferred = $q.defer();
                    var body = {
                        'aws_access_key_id': accessKey,
                        'aws_secret_access_key': secretKey
                    }

                    $http({
                        method: "POST",
                        url: UrlService + 'authenticate',
                        data: body,
                        headers: {'Content-Type': 'application/json'}
                    })
                        .then(
                            function (result) {
                                console.log("result");
                                console.log(result);
                                if (result.status === 200) {
                                    $window.localStorage['userInfo'] = JSON.stringify(body)
                                    deferred.resolve(result);
                                }
                                else {

                                }
                            },
                            function (error) {
                                deferred.reject(error);
                            })
                    return deferred.promise;
                }

                return {
                    login: login
                };
            }
        ])
})();
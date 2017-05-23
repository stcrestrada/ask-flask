(function () {
    'use strict';

    angular.module('askFlaskApp')
        .factory('InstanceService', [
            "$http", "$q", "UrlService","$window", function ($http, $q, UrlService, $window) {

                function getInstances() {
                    var deferred = $q.defer();

                    $http({
                        method: "GET",
                        url: UrlService + 'instances',
                        data: "",
                        headers: {'Content-Type': 'application/json', "userInfo": $window.localStorage['userInfo']},
                    })
                        .then(
                            function (result) {
                                if (result.status === 200) {
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
                    getInstances: getInstances
                };
            }
        ])
})();
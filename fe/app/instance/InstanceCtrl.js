/**
 * Created by stephenestrada on 5/22/17.
 */
(function () {
    'use strict';

    angular.module('askFlaskApp')
        .controller('InstanceCtrl', ['$state', '$scope', 'InstanceService', '$window', function ($state, $scope, InstanceService, $window) {

            function instances() {
                InstanceService.getInstances().then(
                    function (res) {
                        console.log(res.data);
                        var instance = res.data;
                        $scope.instances = instance
                    }
                )
            }
            instances();

            $scope.logout = function() {
                $window.localStorage.removeItem('userInfo');
                if ($window.localStorage.length === 0) {
                    return true;
                }
            }
        }])
})();
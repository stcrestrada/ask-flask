angular.module('askFlaskApp').factory('UrlService', UrlService);


function UrlService() {
    return "http://0.0.0.0:8000/api/v1/";
}
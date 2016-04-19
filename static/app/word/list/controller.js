var listModule = angular.module('listModule', [
    'restangular'
]);

listModule.controller('ListController', function ($scope, Restangular) {

    var libraries = Restangular.all('api/library');
    libraries.getList().then(function (result) {
        $scope.libraries = {};
        for (var lib = 0; lib < result.length; lib++) {
            $scope.libraries[result[lib].id] = result[lib]
        }
    });

    var words = Restangular.all('api/vocabulary');
    words.getList().then(function (result) {
        $scope.vocabulary = result;
    });

});
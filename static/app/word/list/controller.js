var listModule = angular.module('listModule', [
    'restangular'
]);

listModule.controller('ListController', function ($scope, Restangular) {

    var words = Restangular.all('api/vocabulary/');
    $scope.getVocabulary = function () {
        var query_params = {
            lib: $scope.settings.checkedLibraries
        };
        words.getList(query_params).then(function (result) {
            $scope.vocabulary = result;
        });
    };

    $scope.getVocabulary();

});
var listModule = angular.module('listModule', [
    'smart-table',
    'restangular',
    'utils'
]);

listModule.controller('ListController', function ($scope, Restangular, UtilsService) {

    $scope.displayedCollection = [];

    $scope.wordVoice = function (word) {
        UtilsService.textToSpeech(word.english);
    };

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
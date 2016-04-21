var listModule = angular.module('listModule', [
    'restangular',
    'utils'
]);

listModule.controller('ListController', function ($scope, Restangular, UtilsService) {

    $scope.wordVoice = function (word) {
        UtilsService.textToSpeech(word.word);
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
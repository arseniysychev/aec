var vocabularyModule = angular.module('vocabularyModule', [
    'restangular'
]);

vocabularyModule.controller('VocabularyController', function ($scope, Restangular) {

    $scope.levels = {};
    $scope.libraries = {};
    $scope.checkBoxLib = {};
    $scope.settings = {
        filterLibraryShow: false,
        checkedLibraries: []
    };

    $scope.checkedLevelsChange = function (item) {
        if ($scope.checkBoxLib[item]) {
            $scope.settings.checkedLibraries.push(item);
        } else {
            var index = $scope.settings.checkedLibraries.indexOf(item);
            $scope.settings.checkedLibraries.splice(index, 1);
        }
    };

    Restangular.all('api/library/').getList().then(function (result) {

        for (var lib = 0; lib < result.length; lib++) {
            $scope.libraries[result[lib].id] = result[lib];

            var level = result[lib].level;
            if (level in $scope.levels) {
                $scope.levels[level].lib.push(result[lib])
            } else {
                $scope.levels[level] = {
                    level: result[lib].level,
                    show: false,
                    lib: new Array(result[lib])
                };
            }
        }
    });

});
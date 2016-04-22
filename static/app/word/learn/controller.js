var learnModule = angular.module('learnModule', [
    'ui.bootstrap',
    'restangular',
    'utils'
]);

learnModule.directive('equal', function () {
    return {
        require: 'ngModel',
        link: function (scope, elm, attrs, ctrl) {
            ctrl.$validators.integer = function (modelValue, viewValue) {
                var answer = scope.$eval(attrs.equal);
                if (answer && answer.length > 0) {
                    var answerList = [answer, answer.trimLeft(), answer.trimLeft('to '), answer.trimLeft('(to) ')];
                    if (answerList.indexOf(viewValue) != -1) {
                        return true
                    }
                }
                return false;
            };
        }
    };
});

String.prototype.trimLeft = function (charlist) {
    if (charlist === undefined)
        charlist = "\s";
    return this.replace(new RegExp("^[" + charlist + "]+"), "");
};

learnModule.controller('LearnController', function ($scope, Restangular, UtilsService) {

    var words = Restangular.all('api/vocabulary');

    $scope.wordVoice = function (word) {
        if ($scope.translateForm.input_word.$invalid) {
            word.help = true;
        }
        UtilsService.textToSpeech(word.english);
    };

    $scope.successForm = function () {
        var query_params = {};
        if ($scope.word && !$scope.word.help) {
            query_params.id = $scope.word.id;
        }

        $scope.getRandomWord(query_params);
    };

    $scope.getRandomWord = function (add_query_params) {

        var query_params = {
            lib: $scope.settings.checkedLibraries
        };

        if ($scope.translateForm) {
            $scope.input_word = null;
            $scope.input_antonym = null;
            $scope.translateForm.input_word.$setPristine();
            $scope.translateForm.input_antonym.$setPristine();
        }

        if (add_query_params) {
            angular.forEach(add_query_params, function (value, key) {
                query_params[key] = value;
            });
        }

        words.one('random/').get(query_params).then(
            function (result) {
                $scope.word = result;
                $scope.word.help = false;
            }
        );
    };

    $scope.getRandomWord();

});
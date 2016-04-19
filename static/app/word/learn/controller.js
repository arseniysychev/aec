var learnModule = angular.module('learnModule', [
    'ui.bootstrap',
    'restangular'
]);

learnModule.directive('equal', function () {
    return {
        require: 'ngModel',
        link: function (scope, elm, attrs, ctrl) {
            ctrl.$validators.integer = function (modelValue, viewValue) {
                if (scope.$eval(attrs.equal)) {
                    if (scope.$eval(attrs.equal) == viewValue) {
                        return true
                    }
                }
                return false;
            };
        }
    };
});

learnModule.directive('customPopover', function () {
    return {
        restrict: 'A',
        template: '<span>{{label}}</span>',
        link: function (scope, el, attrs) {
            scope.label = attrs.popoverLabel;
            $(el).popover({
                trigger: 'click',
                html: true,
                content: attrs.popoverHtml,
                placement: attrs.popoverPlacement
            });
        }
    };
});


String.prototype.trimLeft = function (charlist) {
    if (charlist === undefined)
        charlist = "\s";
    return this.replace(new RegExp("^[" + charlist + "]+"), "");
};

learnModule.controller('LearnController', function ($scope, Restangular) {

    Restangular.all('api/library').getList().then(function (result) {
        $scope.libraries = {};
        for (var lib = 0; lib < result.length; lib++) {
            $scope.libraries[result[lib].id] = result[lib]
        }
    });

    var words = Restangular.all('api/vocabulary');

    $scope.getRandomWord = function (form) {

        if (form) {
            $scope.input_word = null;
            $scope.input_antonym = null;
            form.input_word.$setPristine();
            form.input_antonym.$setPristine();
        }

        words.one('random').get().then(
            function (result) {
                $scope.word = result;
                $scope.word.english = result.word.trimLeft('to ');
            }
        );
    };

    $scope.getRandomWord();

});
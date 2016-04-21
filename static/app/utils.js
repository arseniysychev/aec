var utils = angular.module('utils', []);

utils.service('UtilsService', function () {

    this.textToSpeech = function (word) {
        responsiveVoice.speak(word, "UK English Female");
    };
});

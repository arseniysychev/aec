var app_path = 'static/app/';

app.config(function ($stateProvider, $urlRouterProvider) {

    // For any unmatched url, send to
    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('main', {
            url: "/",
            templateUrl: app_path.concat('main/main.html'),
            data: {
                'noLogin': true
            }
        })
        .state('vocabulary', {
            url: "/vocabulary",
            templateUrl: app_path.concat('word/page.html'),
            controller: 'VocabularyController',
            data: {
                css: app_path.concat('word/style.css'),
                'noLogin': true
            }
        })
        .state('vocabulary.list', {
            url: "/list",
            templateUrl: app_path.concat('word/list/page.html'),
            controller: 'ListController',
            data: {
                'noLogin': true
            }
        })
        .state('vocabulary.learn', {
            url: "/learn",
            templateUrl: app_path.concat('word/learn/page.html'),
            controller: 'LearnController',
            data: {
                'noLogin': true,
                css: app_path.concat('word/learn/style.css')
            }
        })
});
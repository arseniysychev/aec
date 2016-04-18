var app_path = '/app/';

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
        .state('map', {
            url: "/map",
            templateUrl: app_path.concat('map/map.html'),
            controller: 'MainController',
            data: {
                css: app_path.concat('map/map.css')
            }
        })
        .state('vocabulary', {
            abstract: true,
            // url: "/auth",
            template: "<ui-view/>"
        })
        .state('vocabulary.view', {
            url: "/login",
            templateUrl: app_path.concat('/auth/login.html'),
            data: {
                'noLogin': true
            }
        })
});
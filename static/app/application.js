var app = angular.module('myApp', [
    'ui.router',
    'uiRouterStyles',
    'module_map'
]);


app.factory('Session', function ($http) {
    var Session = {
        data: {},
        user: 'user',
        saveSession: function () {
            /* save session data to db */
        },
        updateSession: function () {
            /* load data from db */

            $http.get('/session/').then(function (r) {
                return Session.data = r;
            });
        }
    };
    Session.updateSession();
    return Session;
});

app.service('SessionService', [
    '$injector',
    function ($injector) {
        "use strict";

        this.checkAccess = function (event, toState, toParams, fromState, fromParams) {
            var $scope = $injector.get('$rootScope'),
                $sessionStorage = $injector.get('Session');
            if (toState.data !== undefined) {
                if (toState.data.noLogin !== undefined && toState.data.noLogin) {

                }
            } else {
                if ($sessionStorage.user) {

                } else {
                    $scope.$state.go('auth.login');
                }
            }
        };
    }
]);

app.run(['$rootScope', '$state', '$stateParams', 'SessionService',
        function ($rootScope, $state, $stateParams, SessionService) {

            $rootScope.$state = $state;
            $rootScope.$stateParams = $stateParams;
            $rootScope.user = null;

            $rootScope.$on('$stateChangeStart',
                function (event, toState, toParams, fromState, fromParams) {

                    SessionService.checkAccess(event, toState, toParams, fromState, fromParams);
                }
            );
        }
    ]
);

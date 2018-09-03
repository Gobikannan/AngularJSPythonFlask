var app = angular.module('app', []);

var g = {panel: 'fifth', file: {}};

app.g = g;

g.switch = function(tab){
	$('[data-tab="'+tab+'"]').click();
	app.g.panel = tab;
};

app.controller('Controller', ['$scope', '$rootScope', '$http', function($scope, $rootScope, $http) {
    var self = $scope;
    self.g = app.g;
    $rootScope.baseServerUrl = 'http://localhost:5000';

    angular.element(document).ready(function(){
        $('.demo.menu .item').tab({history:false});
    });    

    self.switch = function(screen, loadFiles){
          self.g.panel = screen;
          if(loadFiles === true) {
            $rootScope.$broadcast('load-files');
          }
    };
}]);
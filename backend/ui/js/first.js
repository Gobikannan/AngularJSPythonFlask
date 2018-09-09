var app = angular.module('app');
app.controller('FirstCtrl', ['$scope', '$rootScope', '$http', function($scope, $rootScope, $http){
	var self = $scope;

	self.documents = [];
	$rootScope.$on('load-files', function(){
		$http.get('/files').then(function(response){
			self.documents = response.data;
		});
	});

	self.load = function(){
		var fname = this.seldoc;
		$http.post('/file_content', {name: fname}).then(function(response){
			$rootScope.$broadcast('load-document', {name: fname, content: response.data[1]});
			app.g.switch('first');
		});
	};
}]);
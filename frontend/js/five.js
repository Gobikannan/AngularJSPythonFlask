var app = angular.module('app');
app.controller('FifthCtrl', ['$scope', '$rootScope', '$http', function ($scope, $rootScope, $http) {
	$scope.targetLocation = '';
	$scope.freeText = '';
	$scope.fileFormat = 'XLS';
	$scope.selectedApp = undefined;
	$scope.selectedAppId = 0;
	$scope.selectedAppName = '';
	$scope.applications = [];
	$scope.ptasks = [];
	$scope.message = '';

	$scope.loadApplicationNames = function () {
		$('.application-name-dropdown').dropdown();
		$http.get($rootScope.baseServerUrl + '/applications').then(function (response) {
			$scope.applications = response.data;
			var selectedApp = {
				name: 'None',
				id: 0
			};
			$scope.applications.unshift(selectedApp);
		}).catch(function (error) {
			$scope.message ='An error occurred while loading applications.';
		});
	};

	$scope.getIcon = function (type) {
		if(type === 'Input')
			return 'blue edit';
		else if(type === 'Click')
			return 'green file';
		else if(type === 'Navigate')
			return 'gray clone';
		else if(type === 'Verify')
			return 'orange wrench';
			
		return 'red ban';
	};

	$scope.fetchApplication = function () {
		if (!$scope.selectedAppId || parseInt($scope.selectedAppId) === 0) {
			$scope.message = 'Please choose Application.';
			return;
		}
		$scope.ptasks = [];
		angular.forEach($scope.applications, (value, key, obj) => {
			if (value.id === parseInt($scope.selectedAppId)) {
				$scope.selectedAppName = value.name;
				$scope.targetLocation = value.target;
				$scope.freeText = value.setting;
			}
		})

		$http.get($rootScope.baseServerUrl +'/application/' + $scope.selectedAppId).then(function (response) {
			$scope.ptasks = response.data;
		}).catch(function (error) {
			$scope.message ='An error occurred while fetching test cases for the selected application.';
		});
	};

	$scope.save = function (selectedAppId) {
		$scope.selectedAppId = selectedAppId;
		if (!$scope.selectedAppId) {
			$scope.message = 'Please choose Application.';
			return;
		}
		if ($scope.targetLocation === '') {
			$scope.message = 'Please enter Target/Location.';
			return;
		}
		if (!$scope.freeText === '') {
			$scope.message = 'Please enter some description.';
			return;
		}

		var model = {
			fileFormat: $scope.fileFormat,
			target: $scope.targetLocation,
			freeText: $scope.freeText,
			appName: $scope.selectedAppName,
			ptasks: $scope.ptasks
		};

		$http.post($rootScope.baseServerUrl + '/application/' + $scope.selectedAppId, model).then(function (response) {
			$scope.message = 'Test Cases saved successfully.';
		}).catch(function (error) {
			$scope.message ='An error occurred while trying to save test cases for the selected application.';
		});
	};
}]);
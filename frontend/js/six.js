var app = angular.module('app');
app.controller('SixthCtrl', ['$scope', '$rootScope', '$http', function($scope, $rootScope, $http){
	$scope.scenarios = [];
	$scope.selectedScenarioId = 0;
	var selectedApp = { name: 'None', id: 0 };
	$scope.scenarios.unshift(selectedApp);
	$scope.releases = [];
	var selectedNoneRelease = { extid: 'None', id: 0 };
	$scope.releases.unshift(selectedNoneRelease);
	$scope.selectedReleaseId = 0;
	$scope.selectedScenarioName = '';
	$scope.selectedReleaseName = '';
	$scope.selectedReleaseDate;
	$scope.fileFormat = 'XLS';
	$scope.tests = [];
	$scope.message = '';

	$scope.loadScenarioNames = function() {
		$scope.message = '';
		$scope.scenarios = [];
		$('.scenario-name-dropdown').dropdown(({
			onChange: function(value, text, $selectedItem) {
			  // custom action
			  if(value && $scope.selectedScenarioId && parseInt($scope.selectedScenarioId) > 0) {
				  $scope.fetchReleases();
			  }
			}
		  }));
		$http.get($rootScope.baseServerUrl + '/scenarios').then(function (response) {
			$scope.scenarios = response.data;
			$scope.scenarios.unshift(selectedApp);
			$scope.selectedReleaseId = 0;
		}).catch(function (error) {
			$scope.message ='An error occurred while loading scenarios.';
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

	$scope.getPassFailIcon = function (passFail) {
		if(passFail === 'P')
			return 'thumbs up green';
		else if(passFail === 'F')
			return 'thumbs down red';
			
		return 'ban';
	};

	$scope.initFileFormat = function() {
		$('.fileformat-name-dropdown').dropdown();
	};

	$scope.initRelease = function() {
		$('.release-name-dropdown').dropdown();
	};

	$scope.fetchReleases = function() {
		$scope.message = '';
		$scope.releases = [];
		if (!$scope.selectedScenarioId || parseInt($scope.selectedScenarioId) === 0) {
			$scope.message = 'Please choose Scenario.';
			return;
		}
		angular.forEach($scope.scenarios, (value, key, obj) => {
			if (value.id === parseInt($scope.selectedScenarioId)) {
				$scope.selectedScenarioName = value.name;
			}
		})
		$http.get($rootScope.baseServerUrl + '/releases/' + $scope.selectedScenarioId).then(function (response) {
			$scope.releases = response.data;
			$scope.releases.unshift(selectedNoneRelease);
			$scope.selectedReleaseId = 0;
		}).catch(function (error) {
			$scope.message ='An error occurred while loading releases/iterations.';
		});
	};

	$scope.loadTestExects = function() {
		$scope.message = '';
		if (!$scope.selectedScenarioId || parseInt($scope.selectedScenarioId) === 0) {
			$scope.message = 'Please choose Scenario.';
			return;
		}
		if (!$scope.selectedReleaseId || parseInt($scope.selectedReleaseId) === 0) {
			$scope.message = 'Please choose Release.';
			return;
		}
		angular.forEach($scope.releases, (value, key, obj) => {
			if (value.id === parseInt($scope.selectedReleaseId)) {
				$scope.selectedReleaseName = value.extid;
				$scope.selectedReleaseDate = value.date ? (new Date(value.date)).toLocaleDateString() : '';
			}
		})
		$scope.tests = [];
		$http.get($rootScope.baseServerUrl + '/testexecdetails/' + $scope.selectedReleaseId).then(function (response) {
			$scope.tests = response.data;
		}).catch(function (error) {
			$scope.message ='An error occurred while loading test execs.';
		});
	};

	$scope.save = function () {
		$scope.message = '';
		if (!$scope.selectedScenarioId || parseInt($scope.selectedScenarioId) === 0) {
			$scope.message = 'Please choose Scenario.';
			return;
		}
		if (!$scope.selectedReleaseId || parseInt($scope.selectedReleaseId) === 0) {
			$scope.message ='Please choose Release.';
			return;
		}

		var model = {
			fileFormat: $scope.fileFormat,
			releaseName: $scope.selectedReleaseName,
			scenarioName: $scope.selectedScenarioName,
			tests: $scope.tests
		};

		$http.post($rootScope.baseServerUrl + '/testexecdetails/' + $scope.selectedReleaseId, model).then(function (response) {
			$scope.message = 'Scenarios saved successfully.';
		}).catch(function (error) {
			$scope.message ='An error occurred while trying to save the scenario/release test execs.';
		});
	};
}]);
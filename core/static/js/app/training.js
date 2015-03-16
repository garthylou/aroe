var trainingMgt = angular.module('aroeTrainingMgt', []);


trainingMgt.controller('TrainingCtrl', ['$scope', '$http', '$modal', 
                                function($scope, $http, $modal) {
    $scope.training = null;


    $scope.saveTraining = function(training)
    {
      var data = angular.copy(training);
      // The api does not manage time. We have to put only date and ISO formatted.
      data.start = training.start.stripTime().format();
      data.end = training.end?training.end.stripTime().format():training.end;

      $http.put('/api/trainings/'+data.id, data).success(function(result)
        {
         	$('#calendar').fullCalendar('updateEvent', training );
        });
      return training;
    };

    $scope.delete = function(training)
    {
    	$http.delete('/api/trainings/'+training.id).success(function() {
        	$('#calendar').fullCalendar('removeEvents', training.id );
        	$scope.training = null;
      });
    };

    $scope.addNewTraining = function(start, end) {
    	var modalInstance = $modal.open({
			templateUrl: 'modalTrainingNew.html',
			controller : ModalTrainingNewCtrl,
			size : 'sm',
			resolve : {
				start : function() { 
					return start;
				},
				end : function() {
					return end;
				}
			}
		});

		return modalInstance.result.then(function (localTitle){
			 return localTitle;
		});
    };

}
]);


var ModalTrainingNewCtrl = function($scope, $modalInstance, start, end) {

    $scope.newTraining = {
    	start : start?start.format():start,
    	end : end?end.format():end,
    	title : null
    }
    $scope.ok = function()
    {
    	$modalInstance.close($scope.newTraining.title);
    }

    $scope.cancel = function()
    {
    	$modalInstance.dismiss('cancel');
    }
};



/* Front End controller */


var trainings = angular.module('aroeTrainings', []);

members.controller('TrainingCtrl', ['$scope', '$filter', '$http', 
                                function($scope, $filter, $http) {

  $scope.training = null;
}]);
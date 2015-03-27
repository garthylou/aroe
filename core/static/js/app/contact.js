var contactModule = angular.module('aroeContact', ['ngSanitize']);


contactModule.controller('ContactCtrl', ['$scope', '$http', '$modal', 'growl', 
                                function($scope, $http, $modal, growl) {
    $scope.to = "association";
    $scope.accueil = "l'association"

	$scope.openContact = function(to, accueil) {
		if (to) {
			$scope.to = to;
		}
		if (accueil) {
			$scope.accueil = accueil;
		}

    	var modalInstance = $modal.open({
			templateUrl: '/static/contactModal.html',
			controller : ModalContactCtrl,
			scope : $scope,
		});

		modalInstance.result.then(function (result) {
      		//Perform the REST call to send the message to the right people
      		data = {
      			'to':$scope.to,
      			'from':result.from,
      			'message':result.message,
      		}
      		$http.post('/api/contact', data).success(function(result)
        	{
         		//Display message that email was sent.
         		growl.addSuccessMessage(result);
        	})
        	.error(function(result){
        		growl.addErrorMessage(result);
        	});
    	});
    };

                                }]);


var ModalContactCtrl = function($scope, $modalInstance) {

    $scope.ok = function()
    {
    	$modalInstance.close({'from' : $scope.from, 'message' : $scope.message});
    }

    $scope.cancel = function()
    {
    	$modalInstance.dismiss('cancel');
    }
};
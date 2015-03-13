var membersMgt = angular.module('aroeMembersMgt', ['angularFileUpload']);

membersMgt.controller('MembersRowCtrl', ['$scope', '$filter', '$http', '$upload', 
                                function($scope, $filter, $http, $upload) {

  
  $scope.$watch('files', function () {
        $scope.upload($scope.files);
    });

  $scope.reloadUsers = function()
  {
    $http.get('/api/members').success(function(data)
    {
      $scope.users = data;
    })
  }

  $scope.loaduser = function(id)
  {
    $http.get('/api/members/'+id).success(function(data)
    {
      $scope.selecteduser = data;
    });
  }

  $scope.reloadUsers();

  $scope.saveUser = function(data) {
    if (data.id)
    {
      delete data.photo;
      //$scope.user not updated yet
      $http.put('/api/members/1', data).success(function()
        {
          $scope.reloadUsers();
        });
      return data;
    } else {
      delete data.photo;
      $http.post('/api/members', data).success(function() {
        $scope.reloadUsers();
      })
    }
  };

  // remove user
  $scope.delete = function(user) {
      $http.delete('/api/members/'+user.id).success(function() {
        $scope.reloadUsers();
        $scope.selecteduser = null;
      });
  };

  // add user
  $scope.addUser = function() {
    $scope.inserted = {
      family_name: '',
      firstname : '',
      address : '',
      zipcode : '',
      city : '',
      phone : '',
      email : '',
      photo:null
    };
    $scope.selecteduser = $scope.inserted;
    $scope.editableForm.$show();
  };

  $scope.selectUser = function(user){
    $scope.selecteduser = user;
  }

  $scope.upload = function (files) {
        if (files && files.length) {
            for (var i = 0; i < files.length; i++) {
                var file = files[i];
                $upload.upload({
                    url: '/api/avatars/'+$scope.selecteduser.id,
                    file: file,
                    fileFormDataName: 'photo',
                    method : 'PUT',
                }).progress(function (evt) {
                    var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                }).success(function (data, status, headers, config) {
                  $scope.selecteduser.photo = data.photo;
                  //$scope.reloadUsers(); 
                });
            }
        }
    };

}]);











/* Front End controller */


var members = angular.module('aroeMembers', []);

members.controller('MembersDisplayCtrl', ['$scope', '$filter', '$http', 
                                function($scope, $filter, $http) {

  $scope.reloadMembers = function()
  {
    $http.get('/api/members').success(function(data)
    {
      $scope.members = data;
    })
  }

  $scope.reloadMembers();

}]);
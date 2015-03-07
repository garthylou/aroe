var aroeApp = angular.module('aroe', [
	'ngCookies',
	'xeditable',
	'ui.bootstrap',
	'angularFileUpload',
	'aroeMembersMgt',
]);

aroeApp.config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

/*
aroeApp.run(function (editableOptions) {
	editableOptions.theme = 'default'; // bootstrap3 theme. Can be also 'bs2', 'default'
});
*/

aroeApp.run(['$http', '$cookies', function ($http, $cookies) {
	$http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
	$http.defaults.headers.put['X-CSRFToken'] = $cookies.csrftoken;
	$http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
}]);
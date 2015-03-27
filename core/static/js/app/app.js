var aroeApp = angular.module('aroe', [
	'ngCookies',
	'xeditable',
	'ui.bootstrap',
	'angularFileUpload',
	'aroeMembersMgt',
	'aroeTrainingMgt',
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





/* Front end App */

var aroeFrontendApp = angular.module('aroeFrontEnd', [
	'ngCookies',
	'ui.bootstrap',
	'angular-growl',
	'ngAnimate',
	'ngSanitize',
	'aroeMembers',
	'aroeTrainings',
	'aroeContact',
]);

aroeFrontendApp.config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});


aroeFrontendApp.run(['$http', '$cookies', function ($http, $cookies) {
	$http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
	$http.defaults.headers.put['X-CSRFToken'] = $cookies.csrftoken;
	$http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
}]);

aroeFrontendApp.config(['growlProvider', function(growlProvider) {
	growlProvider.globalTimeToLive(10000);
	growlProvider.onlyUniqueMessages(false);
}]);



/// JQUERY hooks

$(document).ready(function() {

	function getCookie(name) {
	    var cookieValue = null;
	    if (document.cookie && document.cookie != '') {
	        var cookies = document.cookie.split(';');
	        for (var i = 0; i < cookies.length; i++) {
	            var cookie = jQuery.trim(cookies[i]);
	            // Does this cookie string begin with the name we want?
	            if (cookie.substring(0, name.length + 1) == (name + '=')) {
	                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                break;
	            }
	        }
	    }
	    return cookieValue;
	}

	function convert(p){
    	var d = $.Deferred();
    	p.then(function(val){
       		d.resolve(val);
    	}, function(err){ 
       		d.reject(err); 
    	});
    	return d.promise();
	}

	$.ajaxSetup({
  		headers: {
    		'X-CSRFToken': getCookie('csrftoken')
  		}
	});

   		// page is now ready, initialize the calendar...

   	if ($('#calendar').fullCalendar) {

    	$('#calendar').fullCalendar({
        // put your options and callbacks here
        	selectable: true,
			selectHelper: true,
			select: function(start, end) {
				var gettingTitle = convert(
					$('[ng-controller="TrainingCtrl"]').scope().addNewTraining(start, end)
					);
				gettingTitle.done(function (title) {
					var eventData;
					if (title) {
						eventData = {
							title: title,
							start: start,
							end: end
						};
						$.ajax({
   							url: '/api/trainings',
   							data: {
   								title : title,
   								start : start.format(),
   								end : end.format()
   							},
   							type: "POST",
   							success : function(result)
   							{
   								$('#calendar').fullCalendar('renderEvent', result);
   								$('#calendar').fullCalendar('unselect');
   							}
   						});
					}
					});
			},
			eventResize : function(calEvent)
			{
				$.ajax({
   						url: '/api/trainings/'+calEvent.id,
   						data: {
   							title : calEvent.title,
   							start : calEvent.start.format(),
   							end : (calEvent.end?calEvent.end.format():calEvent.end)
   						},
   						type: "PUT"
   					});
			},
			eventDrop : function(calEvent)
			{
				$.ajax({
   						url: '/api/trainings/'+calEvent.id,
   						data: {
   							title : calEvent.title,
   							start : calEvent.start.format(),
   							end : (calEvent.end?calEvent.end.format():calEvent.end)
   						},
   						type: "PUT"
   					});
			},
			editable: true,
			eventLimit: true, // allow "more" link when too many events
			events: '/api/trainings',
			eventClick: function(calEvent, jsEvent, view) {
				if($('#calendar').data("lastClick"))
				{
					// Reset the background color to identify the selection
        			$('#calendar').data("lastClick").backgroundColor = '#3b91ad';
        			$('#calendar').fullCalendar('updateEvent', $('#calendar').data("lastClick") );
				}
				$('#calendar').data("lastClick", calEvent);

				// change the background color to identify the selection
        		calEvent.backgroundColor = '#088A08';
        		$('#calendar').fullCalendar('updateEvent', calEvent);
        		
        		// Update the angular model and apply modification.
				$('[ng-controller="TrainingCtrl"]').scope().training = calEvent;
				$('[ng-controller="TrainingCtrl"]').scope().$apply();
				// Do not load the url of the event (change the default behavior of fullcalendar.)
				return false;
   			},
    	});
	}




	if ($('#calendarDisplay').fullCalendar) {

    	$('#calendarDisplay').fullCalendar({
        // put your options and callbacks here
        	selectable: true,
			events: '/api/trainings',
			eventClick: function(calEvent, jsEvent, view) {
				if($('#calendarDisplay').data("lastClick"))
				{
					// Reset the background color to identify the selection
        			$('#calendarDisplay').data("lastClick").backgroundColor = '#3b91ad';
        			$('#calendarDisplay').fullCalendar('updateEvent', $('#calendarDisplay').data("lastClick") );
				}
				$('#calendarDisplay').data("lastClick", calEvent);

				// change the background color to identify the selection
        		calEvent.backgroundColor = '#088A08';
        		$('#calendarDisplay').fullCalendar('updateEvent', calEvent);
        		
        		// Update the angular model and apply modification.
				$('[ng-controller="TrainingCtrl"]').scope().training = calEvent;
				$('[ng-controller="TrainingCtrl"]').scope().$apply();
				// Do not load the url of the event (change the default behavior of fullcalendar.)
				return false;
   			},
    	});
	}


	});
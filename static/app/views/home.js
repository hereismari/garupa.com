
app.controller('home', function($scope) {

	$scope.form = {};

	$scope.toggleForm = function() {
		$('#welcome').fadeOut('slow', function() {
			$('form').fadeIn('slow');
		});
	};

	$scope.submit = function() {

	};
});


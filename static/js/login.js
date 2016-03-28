$(function(){
	$('#btnLogin').click(function(){
		$.ajax({
			url: '/loginUser',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				// redirect to search page on login
				window.location.href = '/search'
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});

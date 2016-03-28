$(function(){
	$('#btnLogin').click(function(){
		$.ajax({
			url: '/loginUser',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
				window.location.href = 'http://127.0.0.1:5000/search';
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});

$(function(){
	$('#btnLogin').click(function(){
		console.log($('form').serialize());
		$.ajax({
			url: '/loginUser',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});

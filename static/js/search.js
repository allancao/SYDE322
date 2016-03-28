$(function(){
$('#btnSearch').click(function() {
    $.ajax({
      url:'/searchResult',
      data:$('form').serialize(),
      type:'POST',
      success:function(response) {
        window.location.href()
      },
      error: function(error) {
        console.log(error);
      }
    });
  });
});
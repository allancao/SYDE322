$(function(){
  $('#btnSearch').click(function(){

    var data = $('form').serialize();
    console.log(data);
    $.ajax({
      url: '/searchResult',
      data: data,
      type: 'POST',
      success: function(response){
        console.log(response)
      },
      error: function(error){
        console.log(error);
      }
    });
  });
});

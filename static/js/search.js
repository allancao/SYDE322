$(function(){
  $('#btnSearch').click(function(){
    var data = $('form').serialize();
    $.ajax({
      url: '/searchResult',
      data: data,
      type: 'POST',
      success: function(data){
        var obj = eval(data);

        $('.courses-table tr').remove();

        for (var i=0; i < obj.length; i++) {
          // var headers = "<tr> <th>Course Name</th> <th><Start Time</th> <th>End Time</th> </tr>"
          var startString = " <tr class=\"course-item\">";
          var title = "<td class=\"course-item-label\"> " + obj[i].title + "</td>";
          var startTime = "<td> " + obj[i].start_time + "</td>";
          var endTime = "<td> " + obj[i].end_time + "</td>";
          var checkbox = "<td> <input type=\"checkbox\" name=\"check\" value=" + obj[i] + "</td>"
          var endString = " </tr>"
          var newItem =  startString + title + startTime + endTime + checkbox + endString;
          console.log(newItem);
          var x = $(newItem).appendTo('.courses-table');
        }
        $('.courses-table').show();
      },
      error: function(error){
        console.log(error);
      }
    });
  });
});

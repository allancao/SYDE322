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
        var headers = "<tr align=\"center\"> <th>Course Name</th> <th>Day</th><th>Start Time</th> <th>End Time</th> </tr><th></th>";
        $(headers).appendTo('.courses-table');
        createTable(obj);
        $('.courses-table').show();
      },
      error: function(error){
        console.log(error);
      }
    });
  });
});

function createTable(obj) {
   for (var i=0; i < obj.length; i++) {
    var startString = " <tr  class=\"course-item\">";
    var title = "<td class=\"course-item-label\"> " + obj[i].title + "</td>";
    var day = "<td> " + obj[i].days + "</td>";
    var startTime = "<td> " + obj[i].start_time + "</td>";
    var endTime = "<td> " + obj[i].end_time + "</td>";
    var checkbox = "<td> <input type=\"checkbox\" name=\"check\" value=" + obj[i] + "</td>"
    var endString = " </tr>"
    var newItem =  startString + title + day + startTime + endTime + checkbox + endString;
    console.log(newItem);
    var x = $(newItem).appendTo('.courses-table');
  }
}



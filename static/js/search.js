var obj = [];
var calObj = [];
$(function(){
  $('#btnSearch').click(function(){
    var data = $('form').serialize();
    $.ajax({
      url: '/searchResult',
      data: data,
      type: 'POST',
      success: function(data){
        obj = eval(data);

        $('.courses-table tr').remove();
        var headers = "<tr align=\"center\"> <th>Course Name</th> <th>Day</th><th>Start Time</th> <th>End Time</th> </tr><th></th>";
        $(headers).appendTo('.courses-table');
        createTable(obj);
        $('.courses-table').show();
        $('#saveClasses').show();
      },
      error: function(error){
        console.log(error);
      }
    });
  });

  $('#saveClasses').click(function () {
    var n = $('#classes').find('input[type="checkbox"]:checked').each(function(){
      var element = $(this).val();
          calObj.push(obj[element]);
          // addToCalendar(obj[element]);
    });
    // $('#hiddenObj').data('calObj', calObj);
    // $.post('/scheduleData', calObj);
    sendData(calObj);
  });

});

function createTable(obj) {
   for (var i=0; i < obj.length; i++) {
    var startString = " <tr  class=\"course-item\">";
    var title = "<td class=\"course-item-label\"> " + obj[i].title + "</td>";
    var day = "<td> " + obj[i].days + "</td>";
    var startTime = "<td> " + obj[i].start_time + "</td>";
    var endTime = "<td> " + obj[i].end_time + "</td>";
    var checkbox = "<td> <input type=\"checkbox\" name=\"check\" value=\"" + i + "\"</td>"
    var endString = " </tr>"
    var newItem =  startString + title + day + startTime + endTime + checkbox + endString;
    var x = $(newItem).appendTo('.courses-table');
  }
}

function addToCalendar(obj) {
  console.log("add to calendar");
  var myCalendar = $('#calendar');
  myCalendar.fullCalendar();
  var myEvent = {
    title: obj.title,
    start: "2016-03-30",
  };

  myCalendar.fullCalendar('renderEvent', myEvent);
}

function sendData(obj) {
  var arr = JSON.stringify(obj);
  var data = {'myArray': arr};
  $.ajax({
      url: '/scheduleData',
      data: data,
      type: 'POST',
      success: function(data){
        swal({   title: "Success!",   text: "Schedule has been updated!",   type: "success",   confirmButtonText: "Cool" });
      },
      error: function(error){
        console.log(error);
      }
    });
}
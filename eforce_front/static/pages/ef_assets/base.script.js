$(document).ready(function() {

  if(location.protocol == 'https:'){
    socket = new WebSocket("wss://" + window.location.host + "/efassets/");
  }else{
    socket = new WebSocket("ws://" + window.location.host + "/efassets/");
  }

  socket.onmessage = function(e) {

      var msg = push_django_msg_notification(JSON.parse(e.data));

      if(msg != ''){
        var notificationDesc = {notificationDesc: msg + "<br/> Please refresh!"}
        $("#pushNotificationTemplate").tmpl(notificationDesc).prependTo("#efassets_notification_wrapper");
      }

  }

});

function push_django_msg_notification(data){

    var return_msg;
    switch(data.created_type) {
        case 'crisis':
            return_msg = create_crisis_alert_msg(data);
            if (return_msg != "") {
               play_notification_sound('sounds/alert3.mp3');
            }
            break;
        case 'group_instruction':
            return_msg = create_group_instruction_msg(data);
            if (return_msg != "") {
               play_notification_sound('sounds/alert2.mp3');
            }
            break;
    }

    return return_msg;
}

function create_crisis_alert_msg(data){
    var return_msg = "";
    return_msg += "Crisis Alert: " + escape_html(data.title);
    return return_msg;
}

function create_group_instruction_msg(data){

    var return_msg = "";

    var psuedo_groupname = $("#user-group-name").text()
    if(psuedo_groupname.trim() == data.readable_to_group_name) {
      return_msg += "<b>" + escape_html(data.for_crisis_title) + "</b><br/>";
      return_msg += "Instruction alert: " + escape_html(data.instruction_text) + "<br/>";
      return return_msg;
    }

    return return_msg;

}

function play_notification_sound(soundpath){
  let audio = new Audio(static_url + soundpath);
  audio.play();
}

function escape_html(str_to_escape) {

  return str_to_escape.replace(/<\/?[^>]+(>|$)/g, "");

}

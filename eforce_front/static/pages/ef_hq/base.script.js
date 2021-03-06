$(document).ready(function() {

  if(location.protocol == 'https:'){
    socket = new WebSocket("wss://" + window.location.host + "/efhq/");
  }else{
    socket = new WebSocket("ws://" + window.location.host + "/efhq/");
  }

  socket.onmessage = function(e) {

      var msg = push_django_msg_notification(JSON.parse(e.data));

      if(msg != ''){
        var notificationDesc = {notificationDesc: msg + "<br/> Please refresh!"};
        $("#pushNotificationTemplate").tmpl(notificationDesc).prependTo("#efhq_notification_wrapper");
      }

  }

});

function push_django_msg_notification(data){

    var return_msg;
    switch(data.created_type) {
        case 'crisis':
            return_msg = create_crisis_alert_msg(data);
            play_notification_sound('sounds/alert3.mp3');
            break;
        case 'crisis_update':
            return_msg = create_crisis_update_msg(data);
            play_notification_sound('sounds/alert2.mp3');
            break;
        case 'combat_strategy':
            return_msg = create_combat_strategy_alert_msg(data);
            play_notification_sound('sounds/alert2.mp3');
            break;
    }

    return return_msg;

}

function create_crisis_alert_msg(data){
    var return_msg = "";
    return_msg += "Crisis Alert: " + escape_html(data.title);
    return return_msg;
}

function create_crisis_update_msg(data){
    var return_msg = "";
    return_msg += "<b>" + escape_html(data.for_crisis_title) + "</b><br/>";
    return_msg += "EF Crisis Update: " + escape_html(data.description) + "<br/>";
    return_msg += "(<i>" + escape_html(data.by_group) + "</i>)";
    return return_msg;
}

function create_combat_strategy_alert_msg(data){
    var return_msg = "";
    return_msg += "<b>" + escape_html(data.for_crisis_title) + "</b><br/>";
    return_msg += "Combat Strategy Update: " + escape_html(data.detail);
    return return_msg;
}

function play_notification_sound(soundpath){
  let audio = new Audio(static_url + soundpath);
  audio.play();
}

function escape_html(str_to_escape) {

  return str_to_escape.replace(/<\/?[^>]+(>|$)/g, "");

}

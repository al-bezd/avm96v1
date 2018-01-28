
function getRandomInRange(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

  var id_chat_room=getRandomInRange(1, 99999999999999)

  var messages =[];
  var chat_mess=[];
  var i=0;
  var p_a='<div class="leadia_widget_msg leadia-widget-message-block leadia-widget-message-me"  style="display: block;"><div class="msg_wrap" style="margin-top:3px;margin-bottom:3px;"><div class="leadia-widget-message-text" data-block-message="true" id="personal_text_id">';
  var p_b='   </div><div class="msg_wrap_corner"></div></div><div class="leadia_msg_time" data-time="Thu Jul 13 2017 09:44:09 GMT+0500 (Пакистан (зима))">Только что</div></div>';
  var c_a=' <div class="leadia_widget_msg leadia-widget-message-block leadia_user_msg" style="display: block;"><div class="msg_wrap user_msg"><div class="leadia-widget-message-text" id="client_text_id_1" data-content="true">';
  var c_b='   </div><div class="msg_wrap_corner"></div><!--<div class="leadia-widget-edit" data-content-editable="true">--></div></div>';


  $("#send_messages_id").click(function(){
    chat_mess=chat_mess+('КЛИЕНТ: '+String($('#leadia_widget_textarea_id').val())+'\n\n');
    messages=messages + (c_a+(String($('#leadia_widget_textarea_id').val()))+c_b);
    chat.innerHTML=messages;
    $('#leadia_widget_textarea_id').val('');

    if(i == 0)
      {
    setTimeout(answer, 3000);
    i=i+1;
      }
    else {
            if(i >= 1)
        {
            setTimeout(answer2, 3000);
            i=i+1;
          }
          else
          {
            if(i >= 2)
              {
                $('#leadia_widget_textarea_id').val('');
                i=i+1;
              };

          };
    };
});

  $('#personal_wid_id_2').change(function(){


  });

  function answer() {
      //cont='{{consultant.rep2}}';
      messages=messages+(p_a+rep2+p_b);
      chat_mess=chat_mess+('КОНСУЛЬТАНТ: '+rep2+'\n\n');
      chat.innerHTML=messages;
}

  function answer2() {
      //cont='{{consultant.rep3}}';
      messages=messages+(p_a+rep3+p_b);
      chat_mess=chat_mess+('КОНСУЛЬТАНТ: '+rep3+'\n\n');
      chat.innerHTML=messages;

      $.ajax({
          type:"POST",
          url:"/chat/",
          data:{
            'id_room':id_chat_room,
            'messages':'',
            'answerway':'',
            'comment':chat_mess,
            'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val()
          },
          //success:searchSuccess, 
          //error:$('#leadia_widget_textarea_id').val(''),
          //error:alert('!'),
          //success:$("#leadia_widget_textarea_id").val()='',
          //success:function(data){
          //  $('#id_table_content').text(data.id_table_content);
          //},
                        
          //error: alert('---'),
          dataType:'html'
          });

    //};
}
$(".leadia_widget_body").hide();
transform_up();

function FirstShow () {
      if ($(".leadia_widget_body").is(":hidden")) { //alert('1');// height:327px
         //if ($(".leadia_widget_body").is('height:0px')) { alert('1');// height:327px
        //$(".leadia_widget_body").slideDown("slow", 1.33);
        transform_down();
        $(".leadia_widget_body").css("display", 'block');
        $(".leadia_widget_body").animate({ height: "327px"}, 150);
      };
 };

setTimeout(FirstShow, 3000);

$(".leadia_widget_body").css('height','0px');
$('#leadia-widget').mouseenter(function () {
      if ($(".leadia_widget_body").is(":hidden")) { //alert('1');// height:327px
         //if ($(".leadia_widget_body").is('height:0px')) { alert('1');// height:327px
        //$(".leadia_widget_body").slideDown("slow", 1.33);
        transform_down();
        $(".leadia_widget_body").css("display", 'block');
        $(".leadia_widget_body").animate({ height: "327px"}, 150);
      };
 });
$('.leadia-widget-worker-name').click(function(){
  //alert("!!!");
  //$(".leadia_widget_body").hide();
      if ($(".leadia_widget_body").is(":hidden")) { // height:327px
        /////$(".leadia_widget_body").show("slow", 0.33);
        transform_down();
          $(".leadia_widget_body").css("display", 'block');
          $(".leadia_widget_body").animate({ height: "327px"}, 150);
      } else {
        transform_up();
        $(".leadia_widget_body").animate({ height: "0px"}, 150);
        //$(".leadia_widget_body").hide('slow', 1.50);

        if($(".leadia_widget_body").css('height','0px'))
          {
            setTimeout(funct_stop, 500);
          };
        

      }
});

function funct_stop(){
  transform_up();
  $(".leadia_widget_body").css("display", 'none');
  
}
  
$('#id_glyphicon-chevron').click(function(){
  //alert("!!!");
  //$(".leadia_widget_body").hide();
      if ($(".leadia_widget_body").is(":hidden")) { // height:327px
        /////$(".leadia_widget_body").show("slow", 0.33);
        transform_down();
          $(".leadia_widget_body").css("display", 'block');
          $(".leadia_widget_body").animate({ height: "327px"}, 150);
      } else {
        $(".leadia_widget_body").animate({ height: "0px"}, 150);
        //$(".leadia_widget_body").hide('slow', 1.50);

        if($(".leadia_widget_body").css('height','0px'))
          {
            setTimeout(funct_stop, 500);
          };
        

      }
});

 function transform_up(){
  $('#id_glyphicon-chevron').removeClass('glyphicon-chevron-down');
  $('#id_glyphicon-chevron').addClass('glyphicon-chevron-up');
}  

 function transform_down(){
  $('#id_glyphicon-chevron').removeClass('glyphicon-chevron-up');
  $('#id_glyphicon-chevron').addClass('glyphicon-chevron-down');
}  

/*
  $("#send_messages_id").click(function(){
    $("#client_wid_id_1").css("display","block");
    $("#client_text_id_1").text($('#leadia_widget_textarea_id').val());
    $('#leadia_widget_textarea_id').val('');
    });

  //if ($("#client_wid_id_1").css("display")=="block")
  $("#leadia_widget_textarea_id").change(function(){
    $("#personal_wid_id_1").css("display","block");
    $("#personal_text_id_1").text("Как вы хотите что бы мы вам ответили? Если хотите что бы мы вам позвонили то просто напишите свой номер, а если хотите что бы ответ пришел вам на почту то просто напишите свой вопрос а адрес электронной почты оставьте в скобочках, вот так (myemail@domain.com), Спасибо за то что с нами ;)");
    });
  if ($("#client_text_id_2").text() == "none")
    {alert('1');};

*/

    //var thing=$('#leadia_widget_textarea_id').val();
        /*$.ajax({
          type:"POST",
          url:"",
          data:{
            'id_chat_room':id_chat_room,
            'chat_room_messages':$('#leadia_widget_textarea_id').val(),
            'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val()
          },
          success:searchSuccess, 
		  error:$('#leadia_widget_textarea_id').val(''),
          //error:alert('!'),
          //success:$("#leadia_widget_textarea_id").val()='',
          //success:function(data){
          //  $('#id_table_content').text(data.id_table_content);
          //},
                        
          //error: alert('---'),
          dataType:'html'
        });*/



    




    function searchSuccess(data, textStatus, jqXHR)
{
  $('#leadia_widget_textarea_id').val('');
  var con=jqXHR.responseText;
  var position_begin=con.indexOf('<begin>');
  var position_end=con.indexOf('</begin>');
  //alert(con);
  //$('#id_consult').html(con.substr(position_begin,position_end));
  $('#id_consult').html(con);
}

console.log('Connected');

function change_profile(){
    console.log('how are you seyed')
    cm=document.querySelector('.kodemeli').getAttribute('value');
    location.assign('change_profile?'+'cm='+cm);
}


function homework_panel_opener(){
    cm=document.querySelector('.kodemeli').getAttribute('value');
    location.assign('panel_homework?cm='+cm);
}


function delete_homework(){
    cm=document.querySelector('.kodemeli').getAttribute('value');
    url_file = document.getElementsByName('url');
    url = url_file[0].getAttribute('value');
    location.assign('homework_delete?url='+url+'&cm='+cm);
}
function enter_class(){
    const button = document.getElementById('enter_class');
    link = button.getAttribute("alink");
    window.open( link , '_blank');
}

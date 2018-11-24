$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var first = 1;
    var startedtime;
    //receive details from server
    socket.on('pumptest', function(msg) {
        if (msg.timer){
        if (first==1){
        $('#pumpstarttime').html("The pump was started @ " + msg.timer);
        first=0;
        console.log("firsttimer");
        }
        $('#time').html(msg.pumptime2off);

    }
    });

// while(true){
//
// console.log("asdfa");
//
// }



});

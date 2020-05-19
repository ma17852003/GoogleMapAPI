var mqtt = require('mqtt');
var opt = {
    address: 'mqtt://127.0.0.1',
    port:1883,
    clientId: 'nodejs'
}
var io = require('socket.io');
var express = require("express");
var app = express();
app.use(express.static('www'));
var server = app.listen(5438);
var sio = io.listen(server);

//Create mqtt connection
var client = mqtt.connect(opt);

client.on('connect', function() {
    console.log('MQTT Server Connected');
    client.subscribe('NCTU-ROOM');
    // client.publish('NCTU-ROOM', 'Hello mqtt')
});

client.on('message', function(topic, msg) {
    // message is Buffer
    console.log('receive: ' + topic + 'topic messages: ' + msg.toString());
    // Client.end()
});

sio.on("connection", function (socket) {
  client.on("message", function (topic, msg) {
    console.log("收到 " + topic + " 主題，訊息：" + msg.toString());
    socket.emit("mqtt", { msg: msg.toString() });
  });
});
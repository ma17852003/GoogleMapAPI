var io = require("socket.io");
var express = require("express");
var app = express();
app.use(express.static('www'));

var server = app.listen(5438, function (req, res) {
    console.log("網站伺服器在5438埠口開工了！");
});

var sio = io(server);

sio.on('connection', function (socket) {
    console.log("Connected");

    // 接收'connection'事件訊息
    socket.on('connection', function (data) {
        console.log('來自Arduino的訊息：' + data.msg);
    });

    // 接收'atime'事件訊息
    socket.on('atime', function (data) {
        console.log('來自Arduino的訊息：' + data.msg);
        // 發送時間資料給前端
        socket.emit('atime', {
            'time': new Date().toJSON()
        });
    });
});
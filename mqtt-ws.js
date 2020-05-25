var mqtt;
var host = 'mosquitto';
var port = 9001;

// onConnect 事件
function onConnect() {
    console.log('connected.');
    var raw_message = 'Hello World!';
    message = new Paho.MQTT.Message(raw_message);
    message.destinationName = '/p/client/upload';
    console.log('sending message: ' + raw_message );
    mqtt.send(message);

    // 订阅 download topic
    var subOptions = {
        qos: 1,
        onSuccess: onSubscribe
    };
    mqtt.subscribe('/p/client/download', subOptions);
}

// 订阅主题成功事件
function onSubscribe(context) {
    console.log('subscribe success');
    console.log(context);
}

// 连接失败事件
function onFailure(message) {
    console.log('connect failed.');
}

// onMessageArrived 事件
function onMessageArrived(message) {
    console.log('new message arrived...');
    console.log(message.payloadString);
}


// 建立 MQTT websocket 连接
function MQTTconnect() {
    console.log('connecting to ' + host + ':' + port);
    mqtt = new Paho.MQTT.Client(host, port, 'clientid');
    var options = {
        timeout: 3,
        onSuccess: onConnect,
        onFailure: onFailure,
        userName: 'client',
        password: '123456',
        mqttVersion: 4
    };
    mqtt.onMessageArrived = onMessageArrived;
    mqtt.connect(options);
}
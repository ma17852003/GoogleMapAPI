from flask import Flask, render_template
import eventlet
from flask_mqtt import Mqtt
from flask_socketio import SocketIO

app = Flask(__name__)
eventlet.monkey_patch()

app.config['MQTT_BROKER_URL'] = 'test.mosquitto.org'
app.config['MQTT_BROKER_PORT'] = 1883
# app.config['MQTT_BROKER_URL'] = '140.113.217.24'
# app.config['MQTT_BROKER_PORT'] = 8080
app.config['MQTT_REFRESH_TIME'] = 1.0

mqtt = Mqtt(app)
socketio = SocketIO(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('eqp/pmp/pump1/data')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    # emit a mqtt_message event to the socket containing the message data
    socketio.emit('mqtt_message', data=data)

@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    print(level, buf)

socketio.run(app, host='localhost', port=5000, use_reloader=True, debug=True)

# if __name__ == '__main__':
#     app.run()


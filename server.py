from flask import Flask, render_template
import eventlet
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap

# eventlet.monkey_patch()
app = Flask(__name__)

# app.config['SECRET'] = 'my secret key'
# app.config['TEMPLATES_AUTO_RELOAD'] = True
# # app.config['MQTT_BROKER_URL'] = '192.168.0.111'
# # app.config['MQTT_BROKER_URL'] = 'test.mosquitto.org'
# app.config['MQTT_BROKER_URL'] = 'broker.hivemq.com'
# app.config['MQTT_BROKER_PORT'] = 1883
# # app.config['MQTT_BROKER_PORT'] = 3000
# # app.config['MQTT_USERNAME'] = ''
# # app.config['MQTT_PASSWORD'] = ''
# app.config['MQTT_KEEPALIVE'] = 5
# app.config['MQTT_TLS_ENABLED'] = False
# # app.config['MQTT_BROKER_URL'] = '140.113.217.24'
# # app.config['MQTT_BROKER_PORT'] = 8080
# app.config['MQTT_REFRESH_TIME'] = 1.0

# Parameters for SSL enabled
# app.config['MQTT_BROKER_PORT'] = 8883
# app.config['MQTT_TLS_ENABLED'] = True
# app.config['MQTT_TLS_INSECURE'] = True
# app.config['MQTT_TLS_CA_CERTS'] = 'ca.crt'

# mqtt = Mqtt(app)
# socketio = SocketIO(app)
# bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

# @mqtt.on_connect()
# def handle_connect(client, userdata, flags, rc):
#     mqtt.subscribe('eqp/pmp/pump1/data')

# @mqtt.on_message()
# def handle_mqtt_message(client, userdata, message):
#     data = dict(
#         topic=message.topic,
#         payload=message.payload.decode()
#     )
#     # emit a mqtt_message event to the socket containing the message data
#     socketio.emit('mqtt_message', data=data)

# @mqtt.on_log()
# def handle_logging(client, userdata, level, buf):
#     print(level, buf)
#     if level == MQTT_LOG_ERR:
#         print('Error: {}'.format(buf))


if __name__ == '__main__':
    # socketio.run(app, host='localhost', port=5000,
    #              use_reloader=True, debug=True)
    app.run()

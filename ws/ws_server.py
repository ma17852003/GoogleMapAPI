"""
## original

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class SimpleEcho(WebSocket):

    def handleMessage(self):
        # echo message back to client
        self.sendMessage(self.data)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('', 9292, SimpleEcho)
server.serveforever()
"""

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

import json
import numpy as np


port = 8000

class SimpleEcho(WebSocket):

    def handleMessage(self):
        global data_rsu0, data_rsu1, data_rsu2, data_car

        msg = json.loads(self.data)

        if msg['device'] == 'RSU0':
            data_rsu0 = msg

        elif msg['device'] == 'RSU1':
            data_rsu1 = msg

        elif msg['device'] == 'RSU2':
            data_rsu2 = msg

        elif msg['device'] == 'car':
            data_car = msg

        elif msg['device'] == 'client0':  # james
            res = data_rsu0['obj_arr'][:]
            res.extend(data_rsu1['obj_arr'])
            res.extend(data_rsu2['obj_arr'])
            res.extend(data_car['obj_arr'])

            self.sendMessage(json.dumps(res))

        elif msg['device'] == 'client1':  # wheelchair
            res = {
                   'RSU0': data_rsu0['has_car'],
                   'RSU1': data_rsu1['has_car'],
                  }
            self.sendMessage(json.dumps(res))

        else:
            self.sendMessage('unknown request')

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

def SimpleServer():
    server = SimpleWebSocketServer('', port, SimpleEcho)
    server.serveforever()


if __name__ == '__main__':
    data_rsu0 = {"device": "RSU0", "has_car": -1.0, "obj_arr": []}
    data_rsu1 = {"device": "RSU1", "has_car": -1.0, "obj_arr": []}
    data_rsu2 = {"device": "RSU2", "has_car": -1.0, "obj_arr": []}
    data_car = {"device": "car", "obj_arr": []}

    SimpleServer()


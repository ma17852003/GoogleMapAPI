
import asyncio
import websockets
from websockets import WebSocketServer
import json
import numpy as np

class NpEncoder(json.JSONEncoder):


    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

res = []

async def handleMessage(websocket, path):
    global data_rsu0, data_rsu1, data_rsu2, data_car, res
    async for dataMsg in websocket:
        # await websocket.recv()
        msg = json.loads(dataMsg)
        # print(msg)
        # print(path)
        
        with open("data.json", "a") as write_file:
            json.dump(msg, write_file)

            # print(msg)
        if msg['device'] == 'RSU0':
            data_rsu0 = msg
            # print(data_rsu0)

        elif msg['device'] == 'RSU1':
            data_rsu1 = msg

        elif msg['device'] == 'RSU2':
            data_rsu2 = msg

        elif msg['device'] == 'car':
            data_car = msg

        else:
            await websocket.send('unknown request')

        
        res = data_rsu0['obj_arr'][:]
        res.extend(data_rsu1['obj_arr'])
        res.extend(data_rsu2['obj_arr'])
        res.extend(data_car['obj_arr'])

        # print(res)
        
        # await websocket.send(json.dumps(res))
        
        # return res

async def send2Client(websocket, path):
    # newMsg = handleMessage(res)
    global res
    print(res)
    await websocket.send(json.dumps(res))
    #     res = 1

    # print(newMsg)
    # await websocket.send("newMsg")



# async def handleConnected(websocket):
#     print(self.address, 'connected')


# async def handleClose(websocket):
#     print(self.address, 'closed')


if __name__ == '__main__':
    data_rsu0 = {"device": "RSU0", "has_car": -1.0, "obj_arr": []}
    data_rsu1 = {"device": "RSU1", "has_car": -1.0, "obj_arr": []}
    data_rsu2 = {"device": "RSU2", "has_car": -1.0, "obj_arr": []}
    data_car = {"device": "car", "obj_arr": []}

    # testing = handleMessage(websockets, websockets)
    # print(testing)

    start_server = websockets.serve(handleMessage, "127.0.0.1", 8000)
    start_server1 = websockets.serve(send2Client, "127.0.0.1", 9999)


    asyncio.get_event_loop().run_until_complete(start_server)

    asyncio.get_event_loop().run_until_complete(start_server1)
    asyncio.get_event_loop().run_forever()

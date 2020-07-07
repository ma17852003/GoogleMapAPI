
import asyncio
import websockets

import time
import json
import numpy as np


# int(np.int64(0))

num_device = 3
device_name = ['RSU0', 'RSU1', 'RSU2']

base_lat, base_lon = 24.786280, 121.001905

end_lat, end_lon = 24.786853, 121.002178
diff_lat, diff_lon = np.abs(end_lat-base_lat), np.abs(end_lon-base_lon)

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


def generate_single(obj, id, base_lat, base_lon, device):
    """ data form
    latlong_tmp = {"object": 'people',
                               "number": id,
                               "lat": lat, "long": lon,
                               "device":device_name,
                               "speed":round(meanspeed, 1),
                               "time2intersection":round(time2intersection,1),
                               'bbox':[tt3, tt1, tt4, tt2]}
    """
    dic = {
        "object": obj,
        "number": id,
        "lat": round(base_lat + np.random.uniform(0, diff_lat), 6),
        "long": round(base_lon + np.random.uniform(0, diff_lon), 6),
        "device": device,
        "speed": round(np.random.uniform(0, 20), 1),
        "time2intersection": round(np.random.uniform(0, 7), 1),
        "bbox": list(np.random.randint(360, size=4)),
    }

    return dic


async def dummydatasend():
    uri = "ws://127.0.0.1:8000"
    async with websockets.connect(uri) as websocket:

        while True:
            for i in range(2):
                for i in range(num_device):
                    # num_people = type(np.float32.random.randint(4))
                    # num_car = type(np.float32.random.randint(2))
                    # num_bike = type(np.float32.random.randint(3))
                    num_people = np.random.randint(4)
                    num_car = np.random.randint(2)
                    num_bike = np.random.randint(3)
                    
                    obj_arr = []
                    for j in range(num_people):
                        dummy = generate_single(
                            'people', j, base_lat, base_lon, device_name[i])
                        obj_arr.append(dummy)

                    for j in range(num_car):
                        dummy = generate_single(
                            'car', j, base_lat, base_lon, device_name[i])
                        obj_arr.append(dummy)

                    for j in range(num_bike):
                        dummy = generate_single(
                            'bike', j, base_lat, base_lon, device_name[i])
                        obj_arr.append(dummy)

                    dummy_msg = {
                        "device": device_name[i],
                        "has_car": -1.0,
                        "obj_arr": obj_arr,
                    }
                    msg_str = json.dumps(dummy_msg, cls=NpEncoder)
                    # ws.send(msg_str)
                    await websocket.send(msg_str)
                    print(msg_str)

                    time.sleep(0.5)



asyncio.get_event_loop().run_until_complete(dummydatasend())

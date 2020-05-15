# Google Map Senser Detection

### Using Flask module
```export FLASK_APP=server.py```

### Run Server
```flask run --host=0.0.0.0```


# MQTT server 
```node mqtt.js```

### Send message with topic "NCTU-ROOM"
```mqtt pub -t 'NCTU-ROOM' -h '127.0.0.1' -m 'from MQTT.js' ```

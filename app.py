from fastapi import FastAPI, HTTPException

app = FastAPI()

readings = [
    {"name": "front-door", "room": "hall", "temp": 27.4, "online": True},
    {"name": "hall-lamp", "room": "hall", "temp": 26.1, "online": True},
    {"name": "attic", "room": "attic", "temp": 31.9, "online": True},
    {"name": "fridge", "room": "kitchen", "temp": 4.2, "online": False},
    {"name": "patio", "room": "outside", "temp": 29.8, "online": True},
]

def average_temp(readings):
    total = 0
    for reading in readings:
        total += reading["temp"]
    avg_t = total / len(readings)
    print(f"\nThe average temp is: {avg_t}")
    return avg_t

average_temp(readings)

def hottest(readings):
    hottest_device = readings[0]
    for reading in readings:
        if reading["temp"] > hottest_device["temp"]:
            hottest_device = reading
    print(f"\nThe hottest device is: {hottest_device}")
    return hottest_device

hottest(readings)

#task 1
@app.get("/devices")
def get_devices():
    return readings

#task 2
@app.get("/devices/hottest")
def get_hottest():
    return hottest(readings)

#task 3
@app.get("/devices/online")
def get_online():
    online_devices = []
    for reading in readings:
        if reading["online"]:
            online_devices.append(reading)
    return online_devices

#task 4
@app.get("/devices/{name}")
def get_device(name: str):
    for reading in readings:
        if reading["name"] == name:
            return reading
    raise HTTPException(status_code=404, detail=f"No device called {name}")

#task 5
@app.get("/stats")
def get_stats():
    return {"average_temperature": round(average_temp(readings), 2)} 

#task 6
@app.post("/devices", status_code=201)
def create_device(device: dict):
    readings.append(device)
    return device

#task 7
@app.get("/rooms/{room}/devices")
def get_room_devices(room: str):
    room_devices = []
    for reading in readings:
        if reading["room"] == room:
            room_devices.append(reading)
    if not room_devices:
        raise HTTPException(status_code=404, detail=f"No room called {room}")
    return room_devices
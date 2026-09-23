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
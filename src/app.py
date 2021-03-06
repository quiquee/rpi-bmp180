#!/usr/bin/python
from flask import Flask, jsonify
from flask_cors import CORS
import Adafruit_BMP.BMP085 as BMP085
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
sensor = BMP085.BMP085()


@app.route('/rest/api/v1.0/temperature', methods=['GET'])
def get_tasks():
    temp = sensor.read_temperature()
    return str(temp)

@app.route('/rest/api/v1.0/pressure', methods=['GET'])
def get_val2():
    return str(sensor.read_pressure() )


@app.route('/debug', methods=['GET'])
def debug():
    output = dict()
    bmp180 = dict()
    bmp180['temperature'] = sensor.read_temperature()
    bmp180['temperatureF'] = (sensor.read_temperature() * 9/5 +32)
    bmp180['pressure'] = sensor.read_pressure() 
    bmp180['altitude'] = sensor.read_altitude()
    return json.dumps(bmp180, ensure_ascii=False)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8888)


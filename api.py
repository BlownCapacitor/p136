import pandas as pd
from flask import Flask, jsonify, request
from data import data
import csv

df = pd.read_csv("PDS2.csv")
rows = []
with open ('PDS2.csv', 'r') as f:
  file = csv.reader(f)
  for row in file:
    rows.append(row)
headers = rows[0]
stardata = rows[1:]

headers[0] = 'row number'

starmass = []
starradius = []
starname = []

for i in stardata:
  starmass.append(i[4])
  starradius.append(i[5])
  starname.append(i[2])
stargravity = []

for index,name in enumerate(starname):
  g = float(starmass[index])
  g2 =  g*5.972e+24
  g3 = g2/(float(starradius[index]))
  g4 = g3*(float(starradius[index]))
  g5 = g4*(6371000*637100)
  g6 = g5*6.674e-11
  stargravity.append(g6)

index = df[1].tolist()
names = df[2].tolist()
distance = df[3].tolist()
mass = df[4].tolist()
radius = df[5].tolist()

app = Flask(__name__)

@app.route("/")

def index():
    return jsonify({
        "Data" : stardata,
        "Message" : "Success",
    }, 250)

@app.route("/star")

def planet():
    name = request.args.get("Star_name")
    stardata2 = next(item for item in data if item["Star_name"] == name)
    return jsonify({
        "Data" : stardata2,
        "Message" : "Success",
    },200)

if __name__ == "__main__":
    app.run()

from flask import Flask
import time as tt
import datetime
import calendar
from werkzeug.serving import run_simple
import requests
import json
import csv
import pandas as pd
from pandas.io.json import json_normalize
import re
from pygeocoder import Geocoder
import pycountry
import flatdict
import arcgis
from arcgis.gis import GIS
from IPython.display import display
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import gzip
import shutil
from math import sin, cos, sqrt, atan2, radians

app = Flask(__name__)

@app.route('/display/<latitude>,<longitude>,<time>,<param>')
def display(latitude, longitude, time, param):
    gis = GIS()
    map1 = gis.map("US", zoomlevel=8)

    def genericfun(latitude, longitude, time):
        try:
            string = f"https://api.darksky.net/forecast/68d70a9cf38161567cc4aec124be92ed/{latitude},{longitude},{time}?exclude=hourly,currently,minutely,alert,flags"
            response = requests.get(string)
            data = response.content
            if len(data) < 140:
                return {}
            else:
                parsed_data = pd.read_json(data.decode('utf-8'))
                new = parsed_data['daily'][0]
                new1 = pd.DataFrame(new)
                new1['lat'] = [latitude] * len(new1)
                new1['long'] = [longitude] * len(new1)
                df = new1
                light = gis.content.import_data(df)
                light.layer.layers = [dict(light.layer)]
                map1.add_layer(light)
                try1 = light.query()
                dfn = try1.df
                del dfn['SHAPE']
                js = dfn.to_json(orient='index')
                jdf = json.loads(js)
                jdf1 = jdf["0"]
                del jdf1["lat"]
                del jdf1["long"]
                del jdf1["summary"]
                return jdf1
        except:
            return {}

    def airfun(latitude, longitude, time):
        try:
            response = requests.get(f"https://api.openaq.org/v1/measurements?coordinates={latitude},{longitude}&radius=28000")
            variable = str(response.content)
            if len(variable) < 140:
                return {}
            else:
                xizz = variable[2:-1].encode('utf-8')
                xiz = xizz.decode('utf-8')
                st1 = re.sub('"unit":".*?",', '', xiz)
                st = re.sub(',"city":".*?"}', '}', st1)
                data = json.loads(st)
                df = json_normalize(data, 'results')
                dict1 = list(df['coordinates'])
                df2 = pd.DataFrame(dict1)
                df['lat'] = df2['latitude']
                df['long'] = df2['longitude']
                del df['coordinates']
                dflist = df['date'].tolist()
                l_data = [i['local'][:10] for i in dflist]
                l_local = [i['local'][20:] for i in dflist]
                del df['date']
                del df['location']
                df4 = pd.DataFrame()
                df4['dates'] = l_data
                df4['local'] = l_local
                df['date'] = df4['dates']
                df['local'] = df4['local']
                epoch = [int(tt.mktime(tt.strptime(str(date), "%Y-%m-%d"))) for date in df['date']]
                df['epocht'] = epoch
                df.to_csv("final.csv")
                df = pd.read_csv('final.csv')
                airpol = gis.content.import_data(df)
                airpol.layer.layers = [dict(airpol.layer)]
                map1.add_layer(airpol)
                try1 = airpol.query().df
                del try1['SHAPE']
                del try1['Unnamed__0']
                time1 = int(time)
                min1 = 99999999999
                newset = set(try1['parameter'])
                newsetl = list(newset)
                valuesl = [0] * len(newsetl)
                for i in range(len(try1['epocht'])):
                    for j in range(len(newsetl)):
                        if newsetl[j] == try1['parameter'][i]:
                            if abs(int(try1['epocht'][i]) - time1) <= min1:
                                min1 = abs(int(try1['epocht'][i]) - time1)
                                valuesl[j] = try1['value'][i]
                                if min1 == 0:
                                    break
                jdf2 = dict(zip(newsetl, valuesl))
                return jdf2
        except:
            return {}

    def Merge(dict1, dict2):
        res = {**dict1, **dict2}
        return res

    final = {
        "latitude": latitude,
        "longitude": longitude,
        "time": time
    }

    if param == "generic":
        final["values"] = genericfun(latitude, longitude, time)
    elif param == "air":
        final["values"] = airfun(latitude, longitude, time)
    elif param == "all":
        jdf1 = genericfun(latitude, longitude, time)
        jdf2 = airfun(latitude, longitude, time)
        final["values"] = Merge(jdf1, jdf2)
    elif param in ["airgeneric", "genericair"]:
        jdf1 = genericfun(latitude, longitude, time)
        jdf2 = airfun(latitude, longitude, time)
        final["values"] = Merge(jdf1, jdf2)

    fin = json.dumps(final)
    return fin

if __name__ == '__main__':
    run_simple('0.0.0.0', 80, app)
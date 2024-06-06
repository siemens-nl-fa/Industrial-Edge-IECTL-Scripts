import json
import subprocess
import os
import sys
import time
os.environ['EDGE_SKIP_TLS'] = '1'

IEM_NAME = "FILL_IN"
IEM_URL  = "https://FILL_IN"
IEM_USER = "FILL_IN" #email
IEM_PWD  = "FILL_IN"

# Setup the devices to install the app
devices_to_install = [
    'IED 1'  
]

# The apps to install n the devices
apps_to_install = [    
    'Common Configurator',
    'Common Import Converter',
    'Databus',
    'Energy Manager',   
    'Flow Creator',
    'Databus Gateway',
    'IIH Essentials',
    'Registry Service',
    'IIH Semantics',    
    'Notifier',
    'OPC UA Connector',
    'Performance Insight',
    'SIMATIC S7 Connector' 
]


subprocess.run([
    "iectl", "config", "add", "iem",
    "--name", IEM_NAME,
    "--url", IEM_URL,
    "--user", IEM_USER,
    "--password", IEM_PWD
], check=True)

# app list
iem_apps = subprocess.run(
    ["iectl", "iem", "catalog", "list"],
    capture_output=True,
    text=True   
).stdout
# print(iem_apps)
iem_apps = json.loads(iem_apps)['data']

#device list
iem_devices = subprocess.run(
    ["iectl", "iem", "device", "list"],
    capture_output=True,
    text=True   
).stdout
# print(iem_devices)
iem_devices = json.loads(iem_devices)['data']


#getting all the details of the app name
def find_appinfo_by_appname( name):
    for obj in iem_apps:       
        if obj.get("title") == name:
            return obj   
    return None

#getting all the details of the device name
def find_deviceinfo_by_devicename( name):
    for obj in iem_devices:        
        if obj.get("deviceName") == name:
            return obj       
    return None



def create_infomap_string():
    data = []
    for deviceName in devices_to_install:
        data.append(find_deviceinfo_by_devicename(deviceName))
    formatted_data = { "devices": [entry['deviceId'] for entry in data] }
    return json.dumps(formatted_data)  
infomapString = create_infomap_string()
# print(infomapString)


for app_name in apps_to_install:   
    appinfo = find_appinfo_by_appname(app_name)
    if appinfo != None:
        print('installing ' + appinfo['title'])
        
        subprocess.run([
            "iectl", "iem", "job", "batch-create",
            "--appid", appinfo['applicationId'],
            "--operation", "installApplication",
            "--infoMap", infomapString            
        ], check=True)



    



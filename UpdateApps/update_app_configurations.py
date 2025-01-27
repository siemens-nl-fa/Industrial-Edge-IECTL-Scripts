import json
import subprocess
import os
import sys
import time
os.environ['EDGE_SKIP_TLS'] = '1'

IEM_NAME = ""
IEM_URL  = ""
IEM_USER = "" #email
IEM_PWD  = ""

APP_ID = "" #leave empty to loop through all App ids
CONFIG_ID = "" #leave empty to loop through all configs
CONFIG_TEMPLATE_ID = ""
DEVICE_ID = "" #Leave empty to get all devices

from lib.config import *
from lib.iem import *

add_iem(IEM_NAME,IEM_URL, IEM_USER, IEM_PWD)

if(APP_ID == ""):
    print('Catalog Apps')
    print(catalog_list())
    app_projects = appproject_listprojects()
    print('Project Apps')
    for project in json.loads(app_projects):
        print( appproject_listapps(project) )
    print('APP_ID is empty, please fill with one of the above')
    exit()

if(CONFIG_ID == "" or CONFIG_TEMPLATE_ID == ""):
    print('Configs of selected apps: ')
    print(appconfig_list(APP_ID))
    exit()

if(DEVICE_ID == ""):
    print('Devices of management:')
    print(device_listapps())
    exit()

operation = "updateAppConfig"
infoMap = { 
    "devices": [DEVICE_ID],
    "configs":[ {
        "configId": CONFIG_ID,
        "templateId": CONFIG_TEMPLATE_ID,
        "editedTemplateText": "UPDATED DATA"
    } ] 
    }
data = "12345"
print( job_batchcreate( APP_ID, operation, infoMap, data ) )


import json
import subprocess
import os
import sys
import time

def catalog_list():    
    iem_apps = subprocess.run(
        ["iectl", "iem", "catalog", "list"],
        capture_output=True,
        text=True   
    ).stdout
    return iem_apps    
    # please put the application id from the apps above as the global variable

def appproject_listprojects():    
    iem_projects = subprocess.run(
        ["iectl", "iem", "app-project", "list-projects"],
        capture_output=True,
        text=True   
    ).stdout
    return iem_projects

def appproject_listapps(Project):    
    iem_apps = subprocess.run(
        ["iectl", "iem", "app-project", "list-apps", "--project-name", Project["name"]],
        capture_output=True,
        text=True   
    ).stdout
    return iem_apps

def appconfig_list(app_id):
    appconfigs = subprocess.run(
        ["iectl", "iem", "app-config", "list", "--id", app_id],
        capture_output=True,
        text=True   
    ).stdout
    return appconfigs

def job_batchcreate(app_id,operation, infoMap, data):
    result = subprocess.run(
        ["iectl", "iem", "job", "batch-create", "--appid", app_id, "--operation", operation, "--infoMap", json.dumps(infoMap)],
        capture_output=True,
        text=True   
    ).stdout
    return result

def device_listapps():
    devices = subprocess.run(
        ["iectl", "iem", "device", "list"],
        capture_output=True,
        text=True   
    ).stdout
    return devices

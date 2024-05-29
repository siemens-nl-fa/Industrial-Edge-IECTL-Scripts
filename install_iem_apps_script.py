import json
import subprocess
import os
import sys
import time

# Fill in these vars
HUB_USER = "FILL_IN"  # Email of the user with API access granted
HUB_API_KEY = "FILL_IN"  # HUB API key
IEM_NAME = "FILL_IN"


# Set environment variables
# os.environ['EDGE_SKIP_TLS'] = str(EDGE_SKIP_TLS)

# Add iehub configuration
subprocess.run([
    "iectl", "config", "add", "iehub",
    "--name", "hub",
    "--url", "https://iehub.eu1.edge.siemens.cloud/",
    "--user", HUB_USER,
    "--password", HUB_API_KEY
], check=True)

# Make a list of all installed apps in the management module
apps = [
    'Cloud Connector',
    'Common Configurator',
    'Common Import Converter',
    'Databus',
    'Energy Manager',
    'External Databus',
    'Flow Creator',
    'IIH Databus Gateway',
    'IHH Essentials',
    'IIH Registry Service',
    'IIH Semantics',    
    'Inventory',
    'Inventory Configurator',
    'Machine Insight',
    'Machine Insight Configurator',
    'Machine Monitor',
    'LiveTwin',
    'Notifier',
    'OPC UA Connector',
    'Performance Insight',
    'SIMATIC S7 Connector',
    'SIMATIC S7+ Connector',
    'WinCC Unified Online Engineering',
    'WinCC Unified Runtime'
]

for app in apps:
    print('###############')    

    try:    
        print('Loading '+app)
        result_update = subprocess.run([
            "iectl", "iehub", "library", "copy-app",
            "--app-name", app,
            "--iem-name", IEM_NAME
        ], 
        check=True, capture_output=True, text=True)
       
        print(result_update.stdout + app)
        time.sleep(1)

    except Exception as e:
        print('ERROR:')    
        print(e)
        print('lets try again...')
        time.sleep(2)
        try:    
            result_update = subprocess.run([
                "iectl", "iehub", "library", "copy-app",
                "--app-name", app,
                "--iem-name", IEM_NAME
            ], 
            check=True,
            capture_output=True,
            text=True)            
            print(result_update.stdout)
            time.sleep(1)

        except Exception as e:
            print('ERROR AGAIN: Not updating.') 
            print(e)



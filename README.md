# Industrial-Edge-IECTL-Scripts
For more information refer to
[https://docs.eu1.edge.siemens.cloud/apis_and_references/iectl/index.html](https://docs.eu1.edge.siemens.cloud/apis_and_references/iectl/index.html)

## Requirements

### Install Industrial Edge Control
1. Extract iectl-linux folder here

2. Install iectl as a command
```bash
sudo install ./iectl-linux/iectl /usr/local/bin/
```


## Script 1: Load all apps to IEM
1. Open install_iem_all_apps.script.py
2. update the fields
    * IEHUB_USER = "FILL_IN" 
    * HUB_API_KEY = "FILL_IN" 
    * IEM_NAME = "FILL_IN" 
3. run command: 
```bash 
python3 install_all_iem_apps_script.py
``` 

## Script 2. Load some apps to IEM
1. Open install_iem_apps.script.py
2. update the fields 
    * IEHUB_USER = "FILL_IN"  
    * HUB_API_KEY = "FILL_IN"
    * IEM_NAME = "FILL_IN" 
3. Add, edit or remove the appnames in the array to change the apps
4. run command: 
```bash 
python3 install_all_iem_apps_script.py
``` 
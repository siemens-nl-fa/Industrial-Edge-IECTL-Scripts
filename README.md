# Industrial-Edge-IECTL-Scripts


## Requirements

1. Install Industrial Edge Control
Extract iectl-linux folder

2. Install iectl as a command
```bash
sudo install ./iectl-linux/iectl /usr/local/bin/
```


## Option: Load all apps to IEM
1. Open install_iem_all_apps.script.py
2. update the fields (FILL IN part)
    * IEHUB_USER = "FILL_IN"  # Email of the user with API access granted
    * HUB_API_KEY = "FILL_IN" # HUB API key
    * IEM_NAME = "FILL_IN" # Name of the management
3. run command: 
```bash 
python3 install_all_iem_apps_script.py
``` 

## Option: Load some apps to IEM
1. Open install_iem_apps.script.py
2. update the fields (FILL IN part)
    * IEHUB_USER = "FILL_IN"  # Email of the user with API access granted
    * HUB_API_KEY = "FILL_IN" # HUB API key
    * IEM_NAME = "FILL_IN" # Name of the management
3. Add, edit or remove the appnames in the array to change the apps
4. run command: 
```bash 
python3 install_all_iem_apps_script.py
``` 
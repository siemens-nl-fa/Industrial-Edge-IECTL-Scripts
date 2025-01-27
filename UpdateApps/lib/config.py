import json
import subprocess
import os
import sys
import time

def add_iem(IEM_NAME,IEM_URL, IEM_USER, IEM_PWD):
    subprocess.run([
        "iectl", "config", "add", "iem",
        "--name", IEM_NAME,
        "--url", IEM_URL,
        "--user", IEM_USER,
        "--password", IEM_PWD
    ], check=True)

from fabric.api import *
# import subprocess
import os


def setup():
    CURRENT_NODE=0
    filename= ""
    env.hosts = ["10.68.47.133","10.68.47.134","10.68.47.135","10.68.47.136","10.68.47.137","10.68.47.138","10.68.47.139","10.68.47.140"]
    env.user = "gpadmin"

def send():
    # run("cd ..")
    # run("chmod 777 /home/gpadmin")
    put("create_ext_table.py")

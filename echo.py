#echo.py
import sys
import urllib2
import json
import os
#=====================
# Write data to stdout
#=====================
x = urllib2.urlopen("http://10.68.47.131:9393/runtime/containers")
response = json.load(x)

container_data = response["_embedded"]["detailedContainerResourceList"]

for cont in container_data:
    if cont["deployedModules"] != []:
        print cont["deployedModules"][0]["name"]
        print cont["deployedModules"][0]["unitName"]
        print cont["attributes"]["ip"]
        node_ip = cont["attributes"]["ip"]
        os.system("scp data5.csv root@" + node_ip + ":/tmp/mycsvdir")

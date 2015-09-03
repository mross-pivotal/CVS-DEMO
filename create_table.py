#echo.py
import sys
from pygresql import pg
import time
import os
import subprocess
import urllib2
import json
#=====================
# Write data to stdout
#=====================
def send(data):
  sys.stdout.write(data)
  # sys.stdout.write(urllib2.urlopen("http://localhost:9393/streams/definitions/pytest").read())
  sys.stdout.write("\n")
  sys.stdout.flush()

#===========================================
# Terminate a message using the default CRLF
#===========================================
def eod():
  send("\r\n")

#===========================
# Main - Echo the input
#===========================

while True:
  try:
    data = raw_input()
    if data:
      d = data.split("\\n")
      schema = 'public' # source2.split("/")[-2]
      filename = 'my_data'
      first_line = d[0]
    # first_line = 'col1, col2, col3'
      values = first_line.split(",")
      hdfs_host = ""
      #data = "ID,Name,Age"
      #d = data.split("\\n")
      #first_line = d[0]
      x= urllib2.urlopen("http://10.68.47.131:9393/streams/definitions/cvsStream").read()
      json_obj = json.loads(x)
      fields = json_obj["definition"].split(" ")
      directoryArr = fields[-2].split("=")
      fileNameArr = fields[-1].split("=")
      fileName= fileNameArr[-1]
      directoryLocation = directoryArr[-1]


      list = " text, \n".join([str(i) for i in values])[:-1] + " text"
      hdfs_source = '/tmp/my_data.csv'
      drop_ext = "DROP EXTERNAL TABLE IF EXISTS " + schema + "." + filename + "_ext;"
      print drop_ext
      ext_table = "CREATE EXTERNAL TABLE " + schema + "." + filename + "_ext (\n" + list + " ) \nLOCATION ( 'pxf://10.68.47.141:8020/" + directoryLocation + "/" + fileName + ".csv" + "?profile=HdfsTextSimple')\nFORMAT '" + filetype + "' \n(HEADER)\nLOG ERRORS INTO errors SEGMENT REJECT LIMIT 2 ;"
      print ext_table
#    print drop_ext
#    print drop_reg
#    print ext_table
#    print reg_table
#    print insert

      print con.query(drop_ext)
      print con.query(ext_table)
      print schema + "." + filename
    #   send(d[0])
      send(data)

      eod()
  except:
    break

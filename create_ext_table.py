# #sink.py
# import sys
#
# while True:
#   try:
#     data = raw_input()
#     if data:
#        #insert a function call here, data is a string.
#        file = open("/Users/mross/workspace/cvs-demo/newfile.txt", "w")
#
#        file.write(data)
#
#     #    file.write("And here is another line\n")
#
#        file.close()
#        print data
#   except EOFError:
#       break
#echo.py
import sys
import json
import os
#=====================
# Execute Create_table on HAWQ Master
#=====================
def send(data):
  parsed_data = data.split("\\n")
  first_line= parsed_data[0]
  os.system("ssh gpadmin@10.68.47.132 python /home/gpadmin/lilypad_final/create_table.py -fl \\'" + first_line + "\\'")
  sys.stdout.write(data)
  sys.stdout.write("my data")
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
      
      parsed_data = data.split("\\n")
      first_line=parsed_data[0]
      os.system("ssh gpadmin@10.68.47.132 python /home/gpadmin/lilypad_final/create_table.py -fl \\'" + first_line + "\\'")
      eod()
  except:
    break

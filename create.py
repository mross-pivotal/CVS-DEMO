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

#=====================
# Write data to stdout
#=====================
def send(data):
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
      
      send(data)
      eod()
  except:
    break

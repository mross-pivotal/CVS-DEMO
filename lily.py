# from pygresql import pg
import psycopg2
import time
import os
import subprocess

########################################################### Currently need to start 2 separate gpfdist process and test pgrep and for loop on lines #####################

# parser = argparse.ArgumentParser()
# parser.add_argument("-rs", help="Specifies what to remove in a string in the case that files have the same prefix")
# parser.add_argument("-ft", help="Specifies the file type of the files being loaded. 'TEXT' will automatically set the column delimited to tab and 'CSV' will be comma delimited")
# args = parser.parse_args()
# if args.rs:
#     replace_string = args.rs
# else:
#     replace_string = ''
# if args.ft:
#     filetype = args.ft
# else:
#     filetype = 'CSV'

# Connection Configuration #
# con = psycopg2.connect('gpadmin', 'localhost', 5432, None, None, 'gpadmin', None)
con = psycopg2.connect( host='10.68.47.132', user="gpadmin", password=None, dbname="gpadmin" )

def init():
    schema = 'public' # source2.split("/")[-2]
    filename = 'my_data'
    first_line = "ID,Name,Age"
    # first_line = 'col1, col2, col3'
    values = first_line.split(",")
    hdfs_host = ""

    list = " text, \n".join([str(i) for i in values])[:-1] + " text"
    hdfs_source = '/tmp/my_data.csv'
    drop_ext = "DROP EXTERNAL TABLE IF EXISTS " + schema + "." + filename + "_ext;"
    print drop_ext
    drop_reg = "DROP TABLE IF EXISTS " + schema + "." + filename + ";"
    print drop_reg
    ext_table = "CREATE EXTERNAL TABLE " + schema + "." + filename + "_ext (\n" + list + " ) \nLOCATION ( 'pxf://10.68.47.141:8020/" + hdfs_source + "?profile=HdfsTextSimple')\nFORMAT '" + filetype + "' \n(HEADER)\nLOG ERRORS INTO errors SEGMENT REJECT LIMIT 2 ;"
    print ext_table
    reg_table = "CREATE TABLE " + schema + "." + filename + " ( " + list + " ) \nDISTRIBUTED RANDOMLY;"
    print reg_table
    insert = "INSERT INTO " + schema + "." + filename + " SELECT * FROM " + schema + "." + filename + "_ext;"
    print insert
#    print drop_ext
#    print drop_reg
#    print ext_table
#    print reg_table
#    print insert

    print con.query(drop_ext)
    print con.query(drop_reg)
    print con.query(ext_table)
    print con.query(reg_table)
    print con.query(insert)
    print schema + "." + filename

init()

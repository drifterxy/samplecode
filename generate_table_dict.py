from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
import csv

config = {
  'user': '',
  'password': '',
  'host': '',
  'database': '',
  'raise_on_warnings': True,
}

try:
  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  cursor.execute("show tables from one15yachtchartering;")
  tablenames = cursor.fetchall()
  print(tablenames)

  with open('tables_dict.csv', 'w', newline='') as csvfile:
     writer = csv.writer(csvfile)
     fieldnames = ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra']
     for tbname in tablenames:
        query = "describe %s;" % tbname
        print(query)
        
        cursor.execute(query)
        tablerows = cursor.fetchall()
        print(tablerows)
        writer.writerow([' '])
        tablename = 'Table %s' % tbname
        writer.writerow([tablename.upper()])
        writer.writerow(fieldnames)
        for row in tablerows:
            writer.writerow(row)

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
import MySQLdb

db = MySQLdb.connect(host="localhost",   # your host 
                     user="arpan",       # username
                     passwd="isha",      # password
                     db="Unknown",  	 # name of the database
		     charset="utf8")     # character set
 
# Create a Cursor object to execute queries.
cur = db.cursor()

table = raw_input('Table Name : ')
table = table + "_Unknown"

cur.execute("delete from " + table)
cur.execute("alter table " + table + " AUTO_INCREMENT = 1")
print "Database Cleared"

db.commit();
cur.close();
db.close();

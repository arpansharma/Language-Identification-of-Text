import MySQLdb

db = MySQLdb.connect(host="localhost",   # your host 
                     user="arpan",       # username
                     passwd="isha",      # password
                     db="Unknown",  	 # name of the database
		     charset="utf8")     # character set
 
# Create a Cursor object to execute queries.
cur = db.cursor()

table = raw_input('Table Name : ')

cur.execute("create table " + table + " ( id int(15) not null auto_increment, word varchar(100) not null, freq int (15) not null, primary key (id))")
cur.execute("ALTER TABLE " + table + " CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci")

print "\nTable Created"

db.commit();
cur.close();
db.close();

import MySQLdb
import re
import enchant

db = MySQLdb.connect(host="localhost",  # your host 
                     user="arpan",      # username
                     passwd="isha",     # password
                     db="lexicon", 	# name of the database
		     charset="UTF8")    # character set
#e = enchant.Dict("en_US")   #English
#d = enchant.Dict("en_GB")   #English
#d = enchant.Dict("fr_FR")   #French
#d = enchant.Dict("de_DE")   #German
#d = enchant.Dict("es_ES")   #Spanish
#d = enchant.Dict("ru_RU")   #Russian

# Create a Cursor object to execute queries.
cur = db.cursor()
table = raw_input("Enter .txt file : ")
file = table + ".txt"
with open(file) as f:
	for line in f:
		a = re.split(r'\t+', line)
		word = a[1]
		freq = a[3]
		#freq = a[2]

		#if d.check(word) or e.check(word):
		#if d.check(word):
		# Select data from table using SQL query.
		cur.execute("INSERT INTO " + table + "(word, freq) VALUES (%s,%s);", (word,freq))		

print ("Database Created")
db.commit() 
cur.close()
db.close()


import MySQLdb
import operator
import string

#Database connectivity for Word List of languages
db = MySQLdb.connect(host="localhost",   # your host 
                     user="arpan",       # username
                     passwd="isha",      # password
                     db="lexicon",  	 # name of the database
		     charset="utf8")     # character set
 
# Create a Cursor object to execute queries.
cur = db.cursor()

#Database connectivity for Unknown languages
db1 = MySQLdb.connect(host="localhost",   # your host 
                     user="arpan",       # username
                     passwd="isha",      # password
                     db="Unknown",  	 # name of the database
		     charset="utf8")     # character set

# Create a Cursor object to execute queries.
cur1 = db1.cursor()

sent = raw_input("Query : ");
#word = sent.split()
word = [x.strip(string.punctuation) for x in sent.split()]

cur.execute("SHOW tables")
tables = []
for (table_name,) in cur:
	a = table_name.encode('ascii', 'ignore')
	tables.append(a);

freq = {"English" : 0, "French" : 0, "Spanish" : 0, "German" : 0, "Russian" : 0, "Latin" : 0}

for table in tables:
	for a in word:		
		cur.execute("SELECT * FROM " + table + " WHERE word like (%s);", (a))	
		  
		if cur.rowcount	!= 0:
			for row in cur.fetchall() :
				freq[table] = freq[table] + row[2]

print "\n"

sorted_freq = sorted(freq.items(), key=operator.itemgetter(1), reverse = True)
print "{:<8} {:<15} ".format('Language','Frequency')
for lang, fr in sorted_freq:
	print "{:<8} {:<15} ".format(lang, fr)

result = max(freq, key=freq.get)
if freq[result] == 0:
	print "\nLanguage is difficult to Identify !\n"
else:
	print "The language of the entered Text is : " + result + "\n"

flag = 0
if freq[result] != 0:
	mispelled = result + "_Unknown"
	for a in word:		
		cur.execute("SELECT * FROM " + result + " WHERE word like (%s);", (a))	
		if cur.rowcount	== 0 :	
			cur1.execute("SELECT * FROM " + mispelled + " WHERE word like (%s);", (a))	
			if cur1.rowcount!= 0 :	
				flag = 1			
				for row in cur1.fetchall() :
					w_freq = row[2]					
					w_freq = row[2] + 1					
					w_freq = str(w_freq)					
					cur1.execute("UPDATE " + mispelled + " SET freq = " + w_freq + " WHERE word = (%s);", (a))	
			else :
				flag = 1
				print a,
				cur1.execute("INSERT INTO " + mispelled + "(word, freq) VALUES (%s,%s);", (a,"1"))
				
		
	if flag == 1:	
		print "\nUnknown / Misspelled words inserted into database\n"

db.commit() 
cur.close()
db.close()

db1.commit() 
cur1.close()
db1.close()


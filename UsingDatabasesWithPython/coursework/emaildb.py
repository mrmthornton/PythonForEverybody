'''
 ^  start of line
 $  end of line
 .  any character
 \s whitespace
 \S Non-whitespace
 *  repeat 0 or more
 *? repeat 0 or more - non greedy
 +  repeat 1 or more
 +? repeat 1 or more - non greedy
 [aeiou] match a single character from the list aeiou
 [^aeiou] match not in list
 [a-z] the match list is a range
 ( start string extraction
 ) end string extaction
'''

import re
import sqlite3

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue # process From lines
    #pieces = line.split()
    #email = pieces[1]
    orgList = re.findall('^From:\s+\S+@(\S+)', line) # extract domain portion of From email
    print orgList
    org = orgList[0]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES ( ?, 1 )''', ( org, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', (org, ))
conn.commit() # This statement commits outstanding changes to disk

# https://www.sqlite.org/lang_select.html

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()


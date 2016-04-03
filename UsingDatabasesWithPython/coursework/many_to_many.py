'''
Created on Mar 27, 2016

@author: mike
'''
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

#import re
import sqlite3
import json

# connect to database and create an input cursor(latin for runner)
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

#cur.execute('''DROP TABLE IF EXISTS Member''') # single command style

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
     id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
     name        TEXT UNIQUE
);

CREATE TABLE Course (
     id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
     title       TEXT UNIQUE
);

CREATE TABLE Member (
    user_id      INTEGER, 
    course_id    INTEGER,
    role         INTERGER,
    PRIMARY KEY (user_id, course_id)
);
''')

fileName = raw_input('Enter file name: ')
if ( len(fileName) < 1 ) : fileName = 'roster_data.json'
stringData = open(fileName).read()
jsonData = json.loads(stringData)

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

for entry in jsonData:
    name = entry[0]
    title = entry[1]
    role = entry[2]
    print name, title
    
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ?', (name, ) )
    user_id = cur.fetchone()[0]
            
    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ?', (title, ) )
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Member (user_id, course_id, role)
        VALUES ( ?, ?, ? )''', ( user_id, course_id, role) )
    
conn.commit() # This statement commits outstanding changes to disk

# https://www.sqlite.org/lang_select.html

cur.close()


''' example SQLite statements '''
"""
SELECT User.name, Member.role, Course.title
FROM User JOIN Member JOIN Course 
ON Member.user_id = User.id AND Member.course_id = Course.id
ORDER BY Course.title, Member.role DESC(descending), User.name
"""



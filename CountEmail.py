import sqlite3
import re
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
fname = 'mbox-short.txt'
#fname = input('Enter file name: ')
#if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
countDict = {}
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    email = re.findall("@.+",email)[0].split('@')[1]
    if(countDict.get(email) == None):
        countDict.update({email : 1})
    else:
        count = countDict.get(email) + 1
        countDict.update({email : count})
print(countDict)
for email in countDict:
    cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, ?)''', (email,countDict.get(email)))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

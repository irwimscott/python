import linecache
import re

startline = 'inicio'
endline = 'fim'
filename = 'teste.txt'

with open(filename) as myFile:
    for num, line in enumerate(myFile, 1):
        if startline in line:
                lastlineofstartnum = num
        #print(lastlineofstartnum)
        #print 'The last line containing',startline,'is:',lastlineofstartnum
                #print "O texto da ultima linha e:",linecache.getline(filename, lastlineofstartnum)
        elif endline in line:
                lastlineofendnum = num
        #print 'The last line containing',endline,'is:',lastlineofendnum
                #print ("O texto da ultima linha e:"), linecache.getline(filename, lastlineofendnum)
myFile.close()

#print(lastlineofstartnum)
#print(lastlineofendnum)

## Now, I need to parse an entire log file, between lastlineofstartnum and lastlineofendnum
## Without the current lines, looking for specific strings.

f = open(filename, 'r')
error_list = ['java.sql.SQLException:']
#error_list = ['java.sql.SQLException:' , 'FATAL' , 'Unable to create connection', 'Failed to create JDBC job repository']
contents=f.read()
f.close()

result = all(elem in contents for elem in error_list)

if result:
    print("Yes, contents contains all elements of error list")
else :
    print("No, contents does not contains all elements of error list")

input_file = open(filename)
for index, line in enumerate(input_file,1):
    # Assuming you start counting from 1
    if lastlineofstartnum <= index <= lastlineofendnum:
        print line
input_file.close()

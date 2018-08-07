import re
f = open('server.log', 'r')
error_list = ['java.sql.SQLException:' , 'FATAL' , 'Unable to create connection', 'Failed to create JDBC job repository']
contents=f.read()
f.close()

result = all(elem in contents for elem in error_list)

if result:
    print("Yes, contents contains all elements of error list")
else :
    print("No, contents does not contains all elements of error list")

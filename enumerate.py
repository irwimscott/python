import linecache
lookup = 'fim'
filename = 'teste.txt'

with open(filename) as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            print 'found at line:', num
            lastlinenum = num
print 'The last line contain', lookup, 'is' , lastlinenum
print 'O texto da ultima linha e: ', linecache.getline(filename, lastlinenum)


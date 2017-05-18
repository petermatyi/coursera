import re
rExp = raw_input("Enter a regular expression: ")
fh = open("mbox.txt")
count = 0
for line in fh :
    line = line.rstrip()
    count = count + len(re.findall(rExp, line))
print "mbox.txt had", count, "lines that matched", rExp
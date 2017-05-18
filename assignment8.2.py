fh = open("mbox-short.txt")
count = 0
for line in fh:
    words = line.split()
    if len(words)!=0:
        if words[0] == 'From':
            print words[1]
            count += 1
print "There were", count, "lines in the file with From as the first word"
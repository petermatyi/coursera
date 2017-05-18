fh = open("mbox-short.txt")
sendAdd = dict()
for line in fh:
    words = line.split()
    if len(words)!=0:
        if words[0] == 'From':
            sendAdd[words[1]] = sendAdd.get(words[1],0) + 1

# print sendAdd

bigAdd = None
bigCount = None

for address,count in sendAdd.items():
    if bigAdd is None or count > bigCount:
        bigAdd = address
        bigCount = count

print bigAdd, bigCount
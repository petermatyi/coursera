# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
confSum = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count+=1
        ind = line.find(" ")
        conf = line[ind:].strip()
        confSum+=float(conf)
av = confSum/count
print 'Average spam confidence:', av
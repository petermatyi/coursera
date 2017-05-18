# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
text = fh.read().upper().rstrip()
print text
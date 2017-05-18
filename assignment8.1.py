fh = open('romeo.txt')
lst = list()
for line in fh:
    newWords = line.split()
    if not lst:
        lst = newWords
    else:
        for word in newWords:
            if word not in lst:
                lst.append(word)
lst.sort()
print lst
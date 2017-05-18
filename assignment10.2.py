fh = open("mbox-short.txt")
hours = dict()
for line in fh:
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        hr = words[5].split(':')
        hours[hr[0]] = hours.get(hr[0], 0) + 1

for k,v in sorted(hours.items()):
    print k, v
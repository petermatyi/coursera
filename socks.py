import socket
import re

while True:
    url = raw_input('Enter URL: ')
    urlParts = re.findall('(\S+)://(\S+?)/(\S+)', url)
    if len(urlParts)!=1:
        print('Wrong format')
        continue
    prot = urlParts[0][0]
    if prot != 'http':
        print('Wrong protocol')
        continue
    host = urlParts[0][1]
    doc = urlParts[0][2]

    try:
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((host, 80))
    except:
        print('Missing host ' + host)
        continue
    try:
        mysock.send('GET ' + url + 'HTTP/1.0\n\n')
        break
    except:
        print('Missing document ')
        continue

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data

mysock.close()
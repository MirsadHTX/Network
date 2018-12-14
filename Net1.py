import socket

myHostName = socket.gethostname()
print(myHostName)

myIpAddress = socket.gethostbyname(myHostName)
print(myIpAddress)

remoteIpAddress = socket.gethostbyname("www.dr.dk")
print(remoteIpAddress)

remoteIpAddress = socket.gethostbyname("www.tv2.dk")
print(remoteIpAddress)

remoteIpAddress = socket.gethostbyname("www.avaz.ba")
print(remoteIpAddress)

remoteIpAddress = socket.gethostbyname("www.python.com")
print(remoteIpAddress)

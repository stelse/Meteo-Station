import socket
import time
import datetime	

port = 8888
ip = "192.168.1.38"

data = "Time: {}\nTemperature: {} C\nHumidity: {} %".format(str(datetime.datetime.now()), -20.5, 0.1)

while True:
	sock = socket.socket()
	sock.connect((ip, port))
	sock.send(data.encode('utf-8'))
	sock.close()

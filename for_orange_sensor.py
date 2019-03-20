from pyA20.gpio import gpio
from pyA20.gpio import port

import RPi.GPIO as GPIO
import dht
import dht
import time
import datetime
import socket
import random

# initialize GPIO
PIN2 = port.PG6
gpio.init()

# read data using pin
#instance = dht.DHT(pin=PIN2)

ip_example = '192.168.1.'
port = 8888

while True:
    time.sleep(2)
    result = instance.read()
    while not result.is_valid():
       result = instance.read()
       print('Invalid data from sensor')
       continue
    text = 'Time: {}\nTemperature: {} C\nHumidity: {} %%'.format(str(datetime.datetime.now()), result.temperature, result.humidity)
    print(text)

    text = str(random.random())
    
    for i in range(101,102):
        try:
            ip = ip_example + str(i)
            print('\t'+ip)
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((ip, port))
            sock.send(text.encode('utf-8'))
            sock.close()

        except Exception as exc:
            print(exc)
            continue
    

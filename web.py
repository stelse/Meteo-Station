from flask import Flask
import socket

port_socket = 8888
port_web = 8080

sock = socket.socket()
sock.settimeout(1)
sock.bind(('', port_socket))
sock.listen(2)

app = Flask(__name__)
@app.route('/')

def temp():
        try:
                conn, addr = sock.accept()
                conn.settimeout(2)
                data = conn.recv(1024).decode('utf-8')
                conn.close()
        except socket.timeout:
                return "Timeout"
        try:
                return data
        except Exception:
                return "No data"


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=port_web)	



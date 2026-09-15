# PROGRAM 46

server.py

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5000))
server.listen(1)

print("Server waiting for connections...")

connection, address = server.accept()
print("Connection with:", address)

message = connection.recv(1024).decode()
print("Client:", message)

connection.close()
server.close()


client.py

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5000))

message = input("Enter message: ")
client.send(message.encode())

client.close()


# PROGRAM 47

server.py

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5000))
server.listen(1)

print("Waiting for client...")

connection, address = server.accept()

message = connection.recv(1024).decode()
print("Client:", message)

response = "Message received successfully!"
connection.send(response.encode())

connection.close()
server.close()


client.py

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5000))

message = input("Enter message: ")
client.send(message.encode())

response = client.recv(1024).decode()
print("Server:", response)

client.close()


# PROGRAM 48

server.py

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5000))
server.listen(1)

print("Waiting for client...")

connection, address = server.accept()

message = connection.recv(1024).decode()
print("Client:", message)

response = "Message received successfully!"
connection.send(response.encode())

connection.close()
server.close()


client.py

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5000))

message = input("Enter message: ")
client.send(message.encode())

response = client.recv(1024).decode()
print("Server:", response)

client.close()


# PROGRAM 49

from ftplib import FTP

ftp = FTP()

host = input("Enter FTP Server: ")
username = input("Enter username: ")
password = input("Enter password: ")

ftp.connect(host, 21)
ftp.login(username, password)

print("Connected successfully")
print("Files and directories")

ftp.retrlines('LIST')

ftp.quit()


# PROGRAM 50

from urllib.request import urlopen
from urllib.parse import urlparse

url = "https://www.example.com/page?id=10"

result = urlparse(url)

print("Scheme:", result.scheme)
print("Domain:", result.netloc)
print("Path:", result.path)
print("Query:", result.query)

response = urlopen(url)
data = response.read()

print("\nWeb page content:")
print(data.decode())


# PROGRAM 51

import smtplib
from email.message import EmailMessage

sender = "your_email@example.com"
receiver = "receiver@example.com"

message = EmailMessage()
message["Subject"] = "Python Lab Test"
message["From"] = sender
message["To"] = receiver

message.set_content("This is email sent using Python SMTP.")

with smtplib.SMTP_SSL("smtp.example.com", 465) as smtp:
    smtp.login(sender, "app_password")
    smtp.send_message(message)

print("Email sent successfully")


# PROGRAM 52

import socket

network = input("Enter network prefix (example 192.168.1): ")

for i in range(1, 255):
    ip = network + "." + str(i)

    try:
        socket.create_connection((ip, 80), timeout=0.2)
        print(ip, "is responsive")

    except (socket.timeout, ConnectionRefusedError, OSError):
        pass


# PROGRAM 53

import socket

host = input("Enter IP address or hostname: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print("\nScanning", host)

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((host, port))

    if result == 0:
        print("Port", port, "is open")

    sock.close()
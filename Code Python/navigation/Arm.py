import pygame
import socket
import time

class Arm():
    def __init__(self, s):
        try:
            client, address = s.accept()
            if(address[0] == '192.168.43.41'):
                print('Arm' + address[0] + ' Connected.')
                self.available = True
                self.client = client
            else:
                client.close()
                client, address = s.accept()
                if(address[0] == '192.168.43.41'):
                    print('Arm' + address[0] + ' Connected.')
                    self.available = True
                    self.client = client
                else:
                    client.close()
                    self.available = False
                    self.client = 0
        except:
            print('Cannot connect to Arm.!!')
            self.available = False
            self.client = 0
        self.angle = 0
    def update(self):
        self.client.send(b'G')
        rec = self.client.recv(100)
        if(rec == '-'):
            pass
        else:
            try:
                self.angle = int(rec)
            except:
                print('Error')
                self.update()
        if(self.angle > 2 and self.angle < 45):
            self.cmp = 50
        elif(self.angle < -2 and self.angle > -45):
            self.cmp = -50
        elif(self.angle >= 45):
            self.cmp = 100
        elif(self.angle <= -45):
            self.cmp = -100
        else:
            self.cmp = 0
        # print(self.angle)

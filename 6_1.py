import time

from itertools import cycle

class TrafficLight:
    def __init__(self):
        self.__color = 'red'



    def running(self, x):
        c = 0
        for i in cycle(x.split()):
            if с > 10:
                break
            if i == '1':
                self.__color == 'red'
                print(self.__color)
                time.sleep(7)
            if i == '2':
                self.__color == 'yellow'
                print(self.__color)
                time.sleep(2)
            if i == '3':
                print('green')
                time.sleep(9)
            с += 1
b=input('Enter sequence, 1 - red, 2- yellow, 3- green: ')
a=TrafficLight()
a.running(b)
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.surname = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn_direction(self):
        print('turn(direction)')
    def show_speed(self):
        print(f'Speed is {self.speed}')
class TownCar(Car):
    def show_speed(self):
        if self.speed>60:
            print(f'Speed limit 60 excedded. Your speed is {self.speed} ')
        else:
            print(f'Speed is {self.speed}')
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Speed limit 40 excedded. Your speed is {self.speed} ')
        else:
             print(f'Speed is {self.speed}')
class PoliceCar(Car):
    pass
new_car1=Car(speed=60, color='red', name='Mercedes1',is_police=False)
new_car1.go()
new_car1.show_speed()
new_car2=TownCar(speed=80, color='yellow', name='Mercedes2',is_police=False)
new_car2.go()
new_car2.show_speed()
new_car3=SportCar(speed=80, color='green', name='Mercedes3',is_police=False)
new_car3.go()
new_car3.show_speed()
new_car4=WorkCar(speed=70, color='red', name='Mercedes4',is_police=False)
new_car4.go()
new_car4.show_speed()
new_car5=PoliceCar(speed=150, color='red', name='Mercedes4',is_police=True)
new_car5.go()
new_car5.show_speed()
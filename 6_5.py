class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('“Запуск отрисовки.”')

class Pen(Stationery):
    def draw(self):
        print('“Запуск отрисовки Pen”')
class Pencil(Stationery):
    def draw(self):
        print('“Запуск отрисовки Pencil”')
class Handle(Stationery):
    def draw(self):
        print('“Запуск отрисовки Handle”')
new_tool=Stationery('St')
new_tool.draw()
new_tool1=Pen('P')
new_tool1.draw()
new_tool2=Pencil('Pencil')
new_tool2.draw()

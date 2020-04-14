class Road:
    def __init__(self, length_road, width_road):
        self._length = length_road
        self._width = width_road

    def calculation(self, weigth, thickness):
        print(f'You need {self._length*self._width*weigth*thickness/1000} tons of asphalt')

my_road=Road(20,5000)
my_road.calculation(25,5)
class Worker:
    def __init__(self, name_worker, surname, position, wage, bonus):
        self.name_w = name_worker
        self.surname = surname
        self.position = position
        self._income={"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        return (self.name_w+' '+ self.surname)

    def get_total_income(self):
        return sum(self._income.values())
my_position=Position(name_worker='Ivan', surname='Ivanov', position='Manager', wage=100, bonus=20)
print(my_position.get_full_name())
print(my_position.get_total_income())
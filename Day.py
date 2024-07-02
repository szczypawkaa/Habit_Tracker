class Day:
    def __init__(self, number, habits=None):
        self._number = number  #który to już dzień chellengu
        self._list_of_habits = habits if habits is not None else []

    def get_number(self):
        return self._number

    def get_list_of_habits(self):
        return self._list_of_habits

    def add_habit(self, habit):
        #dostaję się w ten sposób ponieważ to zmienna private klasy
        self._list_of_habits.append(habit)

    def remove_habit(self, habit):
        # nie usuwa wstecz tylko następne i obecne wystąpienie
        pass



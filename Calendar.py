class Day:
    def __init__(self, date, habits=None):
        self._date = date
        self._list_of_habits = habits if habits is not None else []

    def get_date(self):
        return self._date

    def get_list_of_habits(self):
        return self._list_of_habits

    def add_habit(self, habit):
        #dostaję się w ten sposób ponieważ to zmienna private klasy
        self._list_of_habits.append(habit)

    def remove_habit(self, habit):
        # nie usuwa wstecz tylko następne i obecne wystąpienie
        pass


class Calendar:
    def __init__(self):
        self._list_of_days = []

    def list_of_days(self):
        return self._list_of_days

    def add_day(self, day):
        self._list_of_days.append(day)

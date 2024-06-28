class Day:
    def __init__(self, date, habits = []):
        self._date = date
        self._list_of_habits = habits

    def date(self):
        return self._date

    def list_of_habits(self):
        return self._list_of_habits

    def add_habit(self, habit):
        list_of_habits.append(habit)

    def remove_habit(self, habit):
    # nie usuwa wstecz tylko następne i obecne wystąpienie
        pass



class Calendar:
    def __init__(self):
        self._list_of_days = []

    def list_of_days(self):
        return self._list_of_days

    def add_day(self, day):
        list_of_days.append(day)

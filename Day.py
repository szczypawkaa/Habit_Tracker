class Day:
    def __init__(self, number_in_challenge, date, habits):
        self._number = number_in_challenge  #który to już dzień chellengu
        self._date = date
        #self._day_of_the_week  #z datatime
        self._list_of_habits = habits

    def get_number(self):
        return self._number

    def get_date(self):
        return self._date

    # def set_day_of_the_week(self):
    #     pass

    def get_list_of_habits(self):
        return self._list_of_habits

    def add_habit(self, habit):
        #dostaję się w ten sposób ponieważ to zmienna private klasy
        self._list_of_habits.append(habit)

    def remove_habit(self, habit):
        # nie usuwa wstecz tylko następne i obecne wystąpienie
        pass



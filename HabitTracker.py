class Habit:
    def __init__(self, name, frequency=1, done=0):
        self._name = name
        #częstotliwość oznacza co ile dni ma się powtarzać
        # 1 = codziennie
        # 2 - co drugi dzień (pon, śr, pt, nd, wt, ...)
        self._frequency = frequency
        self._done = False

    def get_name(self):
        return self._name

    def get_frequency(self):
        return self._frequency

    def get_status(self):
        return self._done

    def set_frequency(self, new_f):
        self._frequency = new_f

    #co zrobić z ustawieniem frekwencji na taką samą?
    def set_status(self):
        self._done = not self._done


#jak to zrobić?
# wczytuję całego jsona, tworzę day1 od 1, day2 od 2....,
# potem te dni dodaję do list of days

class HabitTracker:
    def __init__(self):
        self._list_of_days = []
        self._habits_frequency = {} #żeby można było dodawać nowe, zmieniać częstotliwość
        self.current_day = None  #zmienna publiczna
        #sprawdzać czy current_day jest zgodny z datatime i przesuwać dzień

    def get_list_of_days(self):
        return self._list_of_days

    def add_day(self, day):
        self._list_of_days.append(day)

    def add_habit(self):
        pass

    def tick_a_habit(self, habit):
        pass

    # def show_progress(self):
    #     pass

    # def show_strike(self):
    #     pass
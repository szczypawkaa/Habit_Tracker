class Habit:
    def __init__(self, name, frequency=1):
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


        def set_status(self):
            self._done = not self._done


class HabitTracker:
    def __init__(self, calendar):
        self._calendar = calendar

    def add_habit(self):
        pass

    def tick_a_habit(self, habit):
        pass

    def show_progress(self):
        pass

    def show_strike(self):
        pass
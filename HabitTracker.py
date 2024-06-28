class Habit:
    def __init__(self, name, frequency=1):
        self._name = name
        #częstotliwość oznacza co ile dni ma się powtarzać
        # 1 = codziennie
        # 2 - co drugi dzień (pon, śr, pt, nd, wt, ...)
        self._frequency = frequency
        self._
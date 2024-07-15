import json
import datetime
from Day import Day


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
        habit.set_status()

    def set_current_day(self):
        # format daty year-month-day
        latest_day = None
        # today = datatime.datatime.now().strftime("%x")
        today = datetime.date.today()
        if not self._list_of_days.empty(): #czy to potrzebne??
            latest_day = self._list_of_days[-1]
            latest_day = datetime.datetime.strptime(latest_day.get_date(), "%Y-%m-%D")
        if (latest_day != today):
            self.create_days_till_today(latest_day, today)

    def create_days_till_today(self, latest_day, today):
        delta = datetime.timedelta(days=1)
        while (latest_day <= today):
            latest_day += delta


    # def show_progress(self):
    #     pass

    # def show_strike(self):
    #     pass

    def create_days_from_json(self, filename):
        with open(filename, "r") as filehandle:
            data = json.load(filehandle)
        for key in data.keys():
            new_day_of_the_challenge = data[key]["day_of_the_challenge"]
            # new_day_of_the_week = data[key]["day_of_the_week"]
            new_date = data[key]["date"]
            new_list_of_elements_for_habits = data[key]["list_of_habits"]
            real_habits = []
            for element in new_list_of_elements_for_habits:
                name = element["name"]
                frequency = element["frequency"]
                done = element["done"]
                new_habit = Habit(name, frequency, done)
                real_habits.append(new_habit)
            day = Day(new_day_of_the_challenge, new_date, real_habits)
            self._list_of_days.append(day)

    def save_days_to_json(self, filename):
        json_dict = {}
        for day in self._list_of_days:
            formated_habits = []
            for habit in day.get_list_of_habits():
                habit_dict = {
                    "name": habit.get_name(),
                    "frequency": habit.get_frequency(),
                    "done": habit.get_status()
                }
                formated_habits.append(habit_dict)

            json_dict[day.get_number()] = {
                "day_of_the_challenge": day.get_number(),
                "date": day.get_date(),
                "list_of_habits": formated_habits
            }

        with open(filename, "w") as filehandle:
            json.dump(json_dict, filehandle, indent=4)

    def add_days_till_today_to_json(self, filename):
        pass
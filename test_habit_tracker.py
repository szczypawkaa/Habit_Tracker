from HabitTracker import Habit, HabitTracker
from Day import Day
import json


def test_create_habit():
    habit = Habit("running", 3)
    assert habit.get_name() == "running"
    assert habit.get_frequency() == 3
    assert habit.get_status() is False


def test_create_habit_without_frequency():
    habit = Habit("running")
    assert habit.get_name() == "running"
    assert habit.get_frequency() == 1
    assert habit.get_status() is False


def test_habit_set_frequency():
    habit = Habit("running", 3)
    assert habit.get_frequency() == 3
    habit.set_frequency(1)
    assert habit.get_frequency() == 1
    habit.set_frequency(5)
    assert habit.get_frequency() == 5


def test_habit_set_frequency_from_default():
    habit = Habit("running")
    assert habit.get_frequency() == 1
    habit.set_frequency(5)
    assert habit.get_frequency() == 5


def test_habit_set_frequency_to_the_same():
    habit = Habit("running")
    assert habit.get_frequency() == 1
    habit.set_frequency(1)
    assert habit.get_frequency() == 1


def test_habit_set_status():
    habit = Habit("running", 3)
    assert habit.get_status() is False
    habit.set_status()
    assert habit.get_status() is True
    habit.set_status()
    assert habit.get_status() is False


def test_create_days_from_json_file():
    with open("test_days.json", "r") as filehandle:
        data = json.load(filehandle)
    days = []
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
        days.append(day)

    assert len(days) == 3

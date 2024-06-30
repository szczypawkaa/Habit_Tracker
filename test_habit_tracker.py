from HabitTracker import Habit, HabitTracker
from Calendar import Calendar, Day


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


def test_create_day_without_habits():
    monday = Day("1.01")
    assert monday.get_date() == "1.01"

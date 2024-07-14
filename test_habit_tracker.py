from HabitTracker import Habit, HabitTracker


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
    habit_tr = HabitTracker()
    habit_tr.create_days_from_json("test_days.json")
    length = len(habit_tr.get_list_of_days())
    assert length == 3


def test_save_days_to_json_file():
    habit_tr = HabitTracker()
    habit_tr.create_days_from_json("test_days.json")
    habit_tr.save_days_to_json("saved_days.json")

    habit_tr_2 = HabitTracker()
    habit_tr_2.create_days_from_json("saved_days.json")
    length = len(habit_tr_2.get_list_of_days())
    assert length == 3
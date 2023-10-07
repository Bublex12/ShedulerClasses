import os
from datetime import datetime, timedelta
import requests
from spreadsheet_manager import WeeklyLists


def get_info_from_list():
    pass


def transform_lists(list):
    subjects = list[0][0]
    numbers = list[1]

    dict_classes = dict(zip(subjects, numbers))
    schedule_string = "\n".join(f"{number} пара - {subject}" for subject, number in dict_classes.items())

    return schedule_string


def get_info_from_file(name_day):
    timesheet = {"понедельник": WeeklyLists.MONDAY.value,
                 "вторник": WeeklyLists.TUESDAY.value,
                 "среда": WeeklyLists.WEDNESDAY.value,
                 "четверг": WeeklyLists.THURSDAY.value,
                 "пятница": WeeklyLists.FRIDAY.value,
                 "суббота": WeeklyLists.SATURDAY.value}
    try:
        result = transform_lists(timesheet[name_day])
    except KeyError:
        result = 'Нет такого дня недели'

    return result


if __name__ == '__main__':
    get_info_from_file('понедельник')

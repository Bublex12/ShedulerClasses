import os
from datetime import datetime, timedelta
import requests
from spreadsheet_manager import get_range_result_in_sheet,Ranges


def delete_symbol(string):
    string = str(string)
    string = string.replace('[', '')
    string = string.replace("]", "")
    return string


def transform_lists(list):
    subjects = list[0][0]
    numbers = list[1]
    print(subjects, numbers)

    result_dict = {}

    for subject, number in zip(subjects, numbers):
        if subject in result_dict:
            result_dict[subject].append(number)
        else:
            result_dict[subject] = [number]
    schedule_string = "\n".join(f"{delete_symbol(str(number))} пара - {subject}" for subject, number in result_dict.items())
    print(schedule_string)
    return schedule_string


def get_info_from_file(name_day):
    timesheet = {"понедельник": get_range_result_in_sheet(Ranges.MONDAY.value),
                 "вторник": get_range_result_in_sheet(Ranges.TUESDAY.value),
                 "среда": get_range_result_in_sheet(Ranges.WEDNESDAY.value),
                 "четверг": get_range_result_in_sheet(Ranges.THURSDAY.value),
                 "пятница": get_range_result_in_sheet(Ranges.FRIDAY.value),
                 "суббота": get_range_result_in_sheet(Ranges.FRIDAY.value)}
    try:
        result = transform_lists(timesheet[name_day])
    except KeyError:
        result = 'Нет такого дня недели'

    return result


if __name__ == '__main__':
    get_info_from_file('пятница')

from enum import Enum
from googleapiclient.discovery import build
from cred import get_cred
import config


class Ranges(Enum):
    MONDAY = "B2:B9"
    TUESDAY = "C2:C9"
    WEDNESDAY = "D2:D9"
    THURSDAY = "E2:E9"
    FRIDAY = "F2:F9"
    SATURDAY = "G2:G9"


def get_range_result_in_sheet(range_in_sheet_for_day):
    creds = get_cred()
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=config.SAMPLE_SPREADSHEET_ID,
                                range=range_in_sheet_for_day,
                                valueRenderOption="UNFORMATTED_VALUE").execute()
    values = result.get('values', [])
    # print(values)
    max_length = max(len(sublist) for sublist in values)

    # Выравниваем длину каждого вложенного массива
    aligned_arrays = [sublist + [""] * (max_length - len(sublist)) if sublist else [""] * max_length for sublist in
                      values]

    # Суммируем вложенные массивы
    result = [sum(x, []) if isinstance(x[0], list) else x for x in zip(*aligned_arrays)]

    non_empty_indices = [index for index, item in enumerate(result[0]) if item != '']
    result[0] = [item for item in result[0] if item != '']
    array = [result, non_empty_indices]
    return array




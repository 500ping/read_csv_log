import pandas as pd
import glob
from datetime import datetime

start_date = datetime(2023, 2, 7)

# get a list of all CSV files in the directory
file_list = sorted(glob.glob("test-????-??-??.csv"))
print(file_list)


def get_file_list(file_list, start_date):
    for i in range(len(file_list)):
        if datetime.strptime(file_list[i][5:15], '%Y-%m-%d') == start_date or datetime.strptime(file_list[i][5:15], '%Y-%m-%d') > start_date and i <= 0:
            return file_list[i:]
        if datetime.strptime(file_list[i][5:15], '%Y-%m-%d') > start_date and i > 0:
            return file_list[i-1:]
    return []


print(get_file_list(file_list, start_date))

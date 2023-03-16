import pandas as pd
import glob
from datetime import datetime
import time

# start timer
start_time = time.time()

start_date = datetime(2023, 2, 15)

# get a list of all CSV files in the directory
file_list = sorted(glob.glob("test-????-??-??.csv"))


def get_file_list(file_list, start_date):
    for i in range(len(file_list)):
        if datetime.strptime(file_list[i][5:15], '%Y-%m-%d') == start_date or datetime.strptime(file_list[i][5:15], '%Y-%m-%d') > start_date and i <= 0:
            return file_list[i:]
        if datetime.strptime(file_list[i][5:15], '%Y-%m-%d') > start_date and i > 0:
            return file_list[i-1:]
    return []


filtered_files = get_file_list(file_list, start_date)
filtered_files.append("test.csv")

# create an empty list to store dataframes
df_list = []

# loop through each file, read it into a dataframe, and append it to the list
for file in filtered_files:
    df = pd.read_csv(file)
    df_list.append(df)

# concatenate all dataframes in the list into a single dataframe
merged_df = pd.concat(df_list, ignore_index=True)

# print the merged dataframe
print(merged_df)

# convert datetime column to datetime type
merged_df['datetime'] = pd.to_datetime(merged_df['datetime'])

# set datetime column as index
merged_df.set_index('datetime', inplace=True)

# filter dataframe to include only rows from 2023-02-16 to 2023-03-16
start_date = pd.Timestamp(start_date)
merged_df = merged_df.loc[start_date:]

print("-------------")
print(merged_df)

# print the execution time
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")

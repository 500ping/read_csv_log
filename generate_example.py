import csv
import random
from datetime import datetime, timedelta

POINT_OF_TIMES = [
    datetime(2023, 2, 5),
    datetime(2023, 2, 6),
    datetime(2023, 2, 13),
    datetime(2023, 2, 20),
    datetime(2023, 2, 27),
    datetime(2023, 3, 6),
    datetime(2023, 3, 13)
]

for i in range(len(POINT_OF_TIMES) - 1):
    # define start and end dates
    start_date = POINT_OF_TIMES[i]
    end_date = POINT_OF_TIMES[i+1]

    # define time interval (1 second)
    interval = timedelta(seconds=1)

    # open file and create CSV writer
    with open(f'test-{start_date.strftime("%Y-%m-%d")}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # write header row
        writer.writerow(['datetime', 'state'])

        # generate data and write rows
        current_date = start_date
        while current_date < end_date:
            writer.writerow([current_date.strftime(
                '%Y-%m-%d %H:%M:%S'), random.choice((1, 2, 3))])
            current_date += interval

# define start and end dates
start_date = datetime(2023, 3, 13)
end_date = datetime(2023, 3, 17)

# define time interval (1 second)
interval = timedelta(seconds=1)

# open file and create CSV writer
with open('test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # write header row
    writer.writerow(['datetime', 'state'])

    # generate data and write rows
    current_date = start_date
    while current_date <= end_date:
        writer.writerow([current_date.strftime(
            '%Y-%m-%d %H:%M:%S'), random.choice((1, 2, 3))])
        current_date += interval

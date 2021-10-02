import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get high temperatures from this file
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# (0, station), (1, name), (2, date), (3, prcp), (4, tavg), (5, max), (6, tmin)

# plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# format the plot
ax.set_title("Daily high temperatures, July 2018", fontsize=24)
ax.set_xlabel('', fontsize=18)
fig.autofmt_xdate()
ax.set_ylabel('temperature (f)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

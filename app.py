# Temperature Analyzer
#   Create weekly temperature array (Celsius)
#   Convert to Fahrenheit
#   Find hottest & coldest day

import numpy as np
temp = []
num_temp = int(input("Enter the number of temperatures:"))
for i in range(num_temp):
    item = float(input(f"Enter the temperature for day{i+1}:"))
    temp.append(item)
weekly_temp = np.array(temp)
print("All Temperatures in celsius:",weekly_temp)

# Convert to Fahrenheit
fahrenheit_temp = (weekly_temp * 9/5) + 32
print("Temperature in fahrenheit:", fahrenheit_temp)

# Find hottest & coldest day
hottest_day = np.max(weekly_temp)
coldest_day = np.min(weekly_temp)

hottest_index = np.argmax(weekly_temp)
coldest_index = np.argmin(weekly_temp)

print(f"The Hottest day is Day {hottest_index+1} with temperature {hottest_day}\\u00b0C")
print(f"The Coldest day is Day {coldest_index+1} with temperature {coldest_day}\\u00b0C")
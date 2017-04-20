# You look at the clock and it is exactly 2pm. You set an alarm to go off in
# 51 hours. At what time does the alarm go off?

time_in_24hr_format = 2 + 12 + 51 % 24
time_in_12hr_format = time_in_24hr_format

if time_in_12hr_format >= 12:
    time_in_12hr_format %= 12

print(time_in_12hr_format)

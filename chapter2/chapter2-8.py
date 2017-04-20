# Write a Python program to solve the general version of the above problem.
# Ask the user for the time now (in hours), and ask for the number of hours
# to wait. Your program should output what the time will be on the clock when
# the alarm goes off.

hr_current = int(input("Enter the time right now (in hrs): "))
hr_to_wait = int(input("Enter hours to wait: "))

hr_of_alarm =  hr_current + hr_to_wait % 24 # time in 24-hour format

# the next line of codes will print the time in 12-hour format
if hr_of_alarm <= 12:
    print("The alarm will go off at", hr_of_alarm, "AM")
else:
    print("The alarm will go off at", hr_of_alarm % 12, "PM")

# How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow? 

bit32 = (2**32) / 1000 / 60 / 60 / 24
 
print("Okay, let's do something difficult, how many days does it take for a 32-bit system to timeout? ")
print("Easy: ", bit32)
 
 
# How about a 64-bit system? 
 
bit64 = (2**64) / 1000 / 60 / 60 / 24

print("What about a 64-bit system? ")
print("Easy: ", bit64)
 
# My age (33) calculated based on my birthday (March 4th, 1985), using Python modules.

import datetime
currentDate = datetime.datetime.now()

deadline= input ('Plz enter your date of birth (mm/dd/yyyy) ')
deadlineDate= datetime.datetime.strptime(deadline,'%m/%d/%Y')
daysLeft = deadlineDate - currentDate

years = ((daysLeft.total_seconds())/(365.242*24*3600))
yearsInt=int(years)

months=(years-yearsInt)*12
monthsInt=int(months)

days=(months-monthsInt)*(365.242/12)
daysInt=int(days)

hours = (days-daysInt)*24
hoursInt=int(hours)

minutes = (hours-hoursInt)*60
minutesInt=int(minutes)

seconds = (minutes-minutesInt)*60
secondsInt =int(seconds)

print('You are {0:d} years, {1:d}  months, {2:d}  days, {3:d}  hours, {4:d} \
minutes, {5:d} seconds old.'.format(yearsInt,monthsInt,daysInt,hoursInt,minutesInt,secondsInt))

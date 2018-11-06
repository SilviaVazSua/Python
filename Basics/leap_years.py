# This program asks for a starting year and an ending year and then puts all the leap years between them (and including them, if they are also leap years). Leap years are years divisible by 4 (like 1984 and 2004). However, years divisible by 100 are not leap years (such as 1800 and 1900) unless they are also divisible by 400 (such as 1600 and 2000, which were in fact leap years).


start_date = int(input("Tell me a start date, please: "))
end_date = int(input("Tell me a end date, please: "))

end_date2 = end_date + 1

print("The leap years between these two dates (including them) are:")

for dates in range (start_date, end_date2):
	if dates % 4 == 0:
		print (dates)

print("Yes, I know, I'm pretty smart! :D")

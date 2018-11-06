# This program prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”


for x in range(99, 1, -1):
	print( x , "bottles of beer on the wall, ", x, "bottles of beer.")
	x = x - 1
	print("Take one down and pass it around,", x, "bottles of beer on the wall.")
	if x == 1:
		print( x , "bottles of beer on the wall, ", x, "bottles of beer.")
		print("Take one down and pass it around, no more bottles of beer on the wall.")
		print("No more bottles of beer on the wall, no more bottles of beer.") 
		print("Go to the store and buy some more, 99 bottles of beer on the wall.")

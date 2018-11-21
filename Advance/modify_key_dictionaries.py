# We cannot modify any key in a dictionary so, to do that, we have to create a new key-value pair, add the value from the previous key and delete the key we don't want.

my_dict = {
	"a" : 35000, 
	"b" : 8000, 
	"z" : 450	
}

# create new key.value pair
my_dict["new"] = my_dict["a"]

print(my_dict)

# remove key "a"
del(my_dict["a"])

print(my_dict)

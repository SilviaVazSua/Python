# creation a dictionary through a constructor
# my_var = dict()

my_own_dictionary = dict(name = "Silvia", quirky_fact = "Flamingos bend their legs at the ankle, not the knee", fav_quote = "if you can\'t' explain it simply, you don\'t understand it well enough.", pet = "myself" )

# access
print("My pet is: " + my_own_dictionary["pet"])

# modify value
my_own_dictionary["pet"] = "dog"
print("I was kidding, my pet is: " +my_own_dictionary["pet"])

#modify key
my_own_dictionary["fav_animal"] = my_own_dictionary["pet"]
del(my_own_dictionary["pet"])

print("This is my info")
print(my_own_dictionary)

# add

print("Where am I from? I added this to my info.")
my_own_dictionary["country"] = "Spain"
print(my_own_dictionary)

 

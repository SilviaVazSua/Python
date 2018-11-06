# This program asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.

name = input("Tell me, what\'s your name? ")
middlename = input("And your middlename? ")
lastname = input("What about your lastname? ")
print("Hello " + name.capitalize() + " " + middlename.capitalize() + " " + lastname.capitalize() + "! Nice to meet you!")

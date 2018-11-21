class Student():
	def __init__(self, name, discord_id, fav_food, dream):

		self.name 		= name
		self.discord_id = discord_id
		self.fav_food 	= fav_food
		self.dream		= dream

	def my_print(self):
		print(self.name + " " + self.discord_id + " " + self.fav_food + " " + self.dream)

# instantiate different students 
s1 = Student("Virginia Balseiro", "yesVirginia", "pasta", "moving to Europe")
s2 = Student("Andreea Visanoiu", "​Andreea[Gold]", "wontonmee", "teaching_university")
s3 = Student("​Cristina Tarantino", "​CristyTarantino[Gold]", "pasta", "being an amazing developer")
s4 = Student("​Jessi_RS", "​Jessi_RS [Gold]#7015", "pasta", "work as developer by end of the year")
s5 = Student("​Sacha Young", "​sacha[Gold]", "french fries", "to return to research")
s6 = Student("​bituin [gold]", "​#7204", "sashimi", "lessen the gender wage gap")

"""
Program: GUI_template.py
Chapter 8 (page 251)
8/7/2024

**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

Template code for ANY GUI-based application in Chapter 8
"""

from breezypythongui import EasyFrame
import random

class GuessingGame(EasyFrame):
	def __init__(self):
		EasyFrame.__init__(self, "Guessing Game 2.0", 260, 180, resizable = False)

		self.hintLabel = self.addLabel(None, 0, 0, 2, sticky = "NSEW")
		self.addLabel("Your guess:", 1, 0)
		self.guessField = self.addIntegerField(None, 1, 1)
		self.nextButton = self.addButton("Next", 2, 0, command=self.NextGuess)
		self.newButton = self.addButton("New Game", 2, 1, command=self.NewGame)

		self.NewGame()

	def NewGame(self):
		self.prevFailPrefix = -1
		self.magicNumber = random.randint(1, 100)
		#print(self.magicNumber)
		self.count = 0
		self.prevGuessValidity = 0 #0 for valid guess, 1 for out of bounds, 2 for not an int
		self.hintLabel["text"] = "Guess a number between 1 and 100 (inclusive)"
		self.guessField.setNumber(random.randint(1, 100))
		self.nextButton["state"] = "normal"

	def NextGuess(self):
		try: #this probably isn't the easiest way to test if a valid number was recieved but oh well
			guess = self.guessField.getNumber() 
		except ValueError: #not an int
			#If the user inputs >1 non-integer guesses in a row, add prefixes to the error message 
			if self.prevGuessValidity == 2: #get fail prefix index & stuff
				self.hintLabel["text"] = self.GetFailPrefix() + f" not an integer {">" if random.random() < 0.1 else ""}:(" #also, 1/10 chance to make the emoticon
			else: #no fail prefix
				self.hintLabel["text"] = "Not an integer :("
				self.prevGuessValidity = 2
				self.prevFailPrefix = -1

		else:
			if guess > 100 or guess < 1: #out of range
				#If the user inputs >1 out of bounds guess in a row, add prefixes to the error message 
				if self.prevGuessValidity == 1:
					if self.prevFailPrefix != -1 and random.random() < 0.008: #small chance to use every prefix because i felt like it
						self.hintLabel["text"] = "Yep, that's outrageously, definitely, totally,\nabsolutely, still, certainly, quite, very, wildly,\nindisputably catastrophically, surely,\nundeniably, undoubtedly, unequivically,\nclearly out of range [1, 100]"
					else:
						self.hintLabel["text"] = self.GetFailPrefix() + " out of range [1, 100]"
				else: #no fail prefix
					self.hintLabel["text"] = "Out of range [1, 100]"
					self.prevGuessValidity = 1
					self.prevFailPrefix = -1

			else: #good!
				self.count += 1
				self.prevGuessValidity = 0
				if guess < self.magicNumber:
					self.hintLabel["text"] = f"Guess #{self.count}: TOO LOW"
				elif guess > self.magicNumber:
					self.hintLabel["text"] = f"Guess #{self.count}: TOO HIGH"
				else:
					self.hintLabel["text"] = f"Hooray! You got it in {self.count} attempt{"s" if self.count > 1 else ""}!"
					self.nextButton["state"] = "disabled"

	def GetFailPrefix(self):
		if self.prevFailPrefix == -1: #There wasn't a previous fail index. Randomly choose one
			self.prevFailPrefix = random.randint(0, 16)
		else: #There was a previous fail index :( Randomly choose one but with no repeats
			i = random.randint(0, 15)
			if i >= self.prevFailPrefix:
				i += 1
			self.prevFailPrefix = i

		return ["Outrageously", "Definitely", "Totally", "Absolutely", "Still", "Yup, that's", "Certainly", "Quite", "Very", "Wildly", "Indisputably", "Catastrophically", "Surely", "Undeniably", "Undoubtedly", "Unequivically", "Clearly"][self.prevFailPrefix]


		

def main():
	GuessingGame().mainloop()

if __name__ == '__main__':
	main()
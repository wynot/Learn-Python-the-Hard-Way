from sys import exit

print "'Ello love! What's your name, then?"
name = raw_input("> ")

print "Name aside, for the purposes of this game you're a man. Cool?"

raw_input("cool. click enter to start.")

def daughter():
	print "This is the daughter. Her name isn't important. She's a fox."
	print "You are struck by her singularly beauiful, inbred complexion."
	print "Do you propose?"
	
	proposal = raw_input("(Y/N) ")
	
	if proposal == "Y" or proposal == "y":
		print "Bold move, hotshot. You are not nearly closely related enough to her to stand a chance. You're not even a cousin!"
		print "You are turned down flat-out."
		print "It's ok though. No sooner has she turned you down than you realize you're gay."
		
		raw_input("Surprised? ")
		
		print "Well, don't be surprised. It happens all the time."
		print "You spend the rest of your life in opulant, hedonistic isolation."
		print "You win. Congratulations."
		exit(0)
	else:
		print "Ah, no worries then."
		print "As fate would have it, you are accidentally castrated in a freak incident involving a plow and a 5 iron."
		print "um. this is awkward. sorry."
		print "The end."
		exit(0)

def h_quarters():
	print "Ah, an heir! Welcome Monsieur %s!" % name
	print "May I get you a cup of tea?"
	
	tea = raw_input("(Y/N) ")
	
	print "Lovely."

	if tea == "Y":
		print "Here's your tea."
		print "Aren't you going to say thank you?"
		
		raw_input("(Say thank you idiot)")
		
		print "Oh, wait a second it's hot!"
		print "AHH! You spat it out all over me!"
		print "You don't even know how to drink tea? You must not be a true heir. To the servents' quarters with you!"
		s_quarters()
	else:
		print "Nevermind the tea, then. Have you met the daughter of the house?"
		daughter()

def wine_blame():
	print "Oh shit. The head butler noticed the wine is missing."
	print "It's your first day. You can't be caught doing that shit."
	print "Do you blame Bates? Or confess?"
	
	blame_choice = raw_input("wtf do you do???? > ")
	
	if "lame" in blame_choice:
		print "Bates gets fired. But the heir knows what happened and he has recently discovered he's gay. He coerces you to sleep with him in order to keep your job. You become a live-in concubine for the master of the house. The end."
		exit(0)
	elif "onfess" in blame_choice:
		print """
		S.
		A.
		C.
		K.
		E.
		D.
		
		Sacked. You just got sacked.
		
		I hope the steel mill down the street is hiring.
		"""
		exit(0)
	else:
		print "None of those were options. Try again."
		wine_blame()


def s_quarters():
	print "Ugh. A servent. You can enter the back way."
	print "You enter the back way. On the way, you see a nice bottle of wine."
	print "You are thirsty. Nobody is looking. Do you take the bottle of wine?"
	
	wine_choice = raw_input("(Y/N) > ")
	
	if wine_choice is "Y" or wine_choice is "y":
		wine_blame()
	elif wine_choice is "N" or wine_choice is "n":
		print "You are a goody two shoes. Enjoy your boring, steady, lifelong employment as an underappreciated servent. The end."
		exit(0)
	else:
		print "Are you an idiot? Try again."
		s_quarters()


def the_abbey():
	print "Welcome to Downton Abbey, %s! Are you a servent or an heir?" % name
	
	position = raw_input("> ")
	if "servent" in position:
		s_quarters()
	elif "heir" in position:
		h_quarters()
	else:
		print "That wasn't an option. Let's try this again."
		the_abbey()


the_abbey()
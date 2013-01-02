import random
story="""You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight."""
question="Which cave will you go into? (1 or 2)"
middle="""You approach the cave...
It is dark and spooky...
A large dragon jumps out in front of you! He opens his jaws
and..."""
die="""Gobbles you down in one bite!"""
play_again="""Do you want to play again? (yes or no)"""
treasure="""Gives you his treasure!"""
cont=1
print(story)
while (cont==1):
	print(question)
	i=input()
	print (middle)
	r=random.randint(1,2)
	if int(i) ==  r:
		print (treasure)
	else:
		print (die)
	print (play_again)

	i2=input()
	if i2== 'yes' or i2 == 'y' :
		continue
	elif i2=="no" or i2=="n":
		cont=0
 

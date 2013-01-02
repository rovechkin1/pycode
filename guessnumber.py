import random
number=random.randint(1,20)
print ("guess a number")
while(1):
	
	guess=input()
	guess=int(guess)
	if number>guess:
		print("number is bigger than your guess")
	elif number<guess:
		print("number is smaller than your guess")		
	else:
		print("you won!The number was "+str(number))		
		break

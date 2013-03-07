import random
drawings=[
'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
,
'''
  +---+
  |   |
  o   |
      |
      |
      |
=========
'''
,
'''
  +---+
  |   |
  o   | 
  |   |
      |
      |
=========
''' 
,
'''
  +---+
  |   | 
  o   |
 /|   |
      |
      |
=========
'''
,
'''
  +---+
  |   |
  o   |
 /|\  |
      |
      |
=========
'''
,
'''
  +---+
  |   |
  o   |
 /|\  |
 /    |
      |
=========
'''
,
'''
  +---+
  |   |
  o   |
 /|\  |
 / \  |
      |
=========
'''
]










words='''ant baboon badger bat bear beaver camel cat clam
cobra cougar coyote crow deer dog donkey duck eagle ferret
fox frog goat goose hawk lion lizard llama mole monkey
moose mouse mule newt otter owl panda parrot pigeon python
rabbit ram rat raven rhino salmon seal shark sheep skunk
sloth snake spider stork swan tiger toad trout turkey
turtle weasel whale wolf wombat zebra'''
def random_word (words):
	cup=words.split()
	return cup[random.randint(0,len (cup)-1)]
	





def check_letter (guess,underscore,letter):
	temp=[0]*len(underscore)
	for i in range (0,len(underscore)):
		temp[i]=underscore[i]
	for i in range (0,len(guess)):
		if guess[i]==letter:
			temp[i]=letter
	return ''.join(temp)





###########main##########

guess=random_word (words)
#print(guess)
win=0
underscore="_"*len (guess)
n=0
while (n<len(drawings)):
	letter=input("guess a letter: ")
	underscore2=check_letter (guess,underscore,letter)
	print (underscore2)
	if underscore2==guess:
		win=1
		print ("you won!")
		break
	elif not  underscore==underscore2:
	
		underscore=underscore2
	else:
		print(drawings[n])
		n=n+1

if win==0:		
	print('you lost:(')














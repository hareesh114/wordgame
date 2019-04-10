import random

def calculateScore(guess):
	exact = 0
	present = 0
	for i in range(len(word)):
		if word[i] == guess[i]:
			exact += 1
		elif guess[i] in word:
			present += 1 
	return exact,present

print("Select word length ")

while True:
	try:
		word_length = int(input())
	except ValueError:
	    print("That's not a number Please try again !")
	    continue
	else:
		break

word_ascii = random.sample(range(97,123),word_length)
word = ''.join(chr(i) for i in word_ascii)

print("You have 100 attempts to guess the word.....All the Best")

for i in range(1,101):
	while True:
		try:	
			guess = input()
			if len(word) == len(guess):
				break
			else:
				raise TypeError
		except TypeError:
			print("word enterd is not of correct length ")
			continue
		

	exact,present = calculateScore(guess)
	
	if exact == word_length:
		print("......HURRY You Got the word........")
		print("      word is  " + guess)
		break

	print("exact: ",end=" ")
	print(exact,end="   present: ")
	print(present)

	if i%10 == 0 and i!=100:
		print("You have completed ",end="")
		print(i,end="")
		print(" number of attempts ",end="")
		print(100-i,end="")
		print("attempts are left")
	

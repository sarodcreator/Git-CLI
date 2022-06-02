# import random module
import random
choices = ['R', 'P', 'S']

print("Winning Rules of the Rock paper scissor game as follows: \n"
								+"Rock vs paper->paper wins \n"
								+ "Rock vs scissor->Rock wins \n"
								+"paper vs scissor->scissor wins \n")

while True:
	print("Enter choice \n R for Rock, \n P for paper, and \n S for scissor \n")
	
	
	choice = input("Player turn: ")
	
	
	if choice == 'R':
		choice_name = 'player(Rock)'
	elif choice == 'P':
		choice_name = 'player(paper)'
	else:
		choice_name = 'player(scissor)'
		
	
	print("Player choice is: " + choice_name)
	print("\nNow its computer turn.......")

	
	comp_choice = random.choices(choices)
	
	
	while comp_choice == choice:
		comp_choice = random.choices(choices)

	
	if comp_choice == 'R':
		comp_choice_name = 'CPU(Rock)'
	elif comp_choice == 'P':
		comp_choice_name = 'CPU(paper)'
	else:
		comp_choice_name = 'CPU(scissor)'
		
	print("Computer choice is: " + comp_choice_name)

	print(choice_name + ':' + comp_choice_name)

	
	if((choice == 'R' and comp_choice == 'P') or
	(choice == 'R' and comp_choice == 'P' )):
		print("paper wins => ", end = "")
		result = "paper"
		
	elif((choice == 'R' and comp_choice == 'S') or
		(choice == 'R' and comp_choice == 'S')):

		print("Rock wins =>", end = "")
		result = "Rock"
	else:
		print("scissor wins =>", end = "")
		result = "scissor"

	
	if result == choice_name:
		print("\n <== Player wins ==>")
	else:
		print("\n <======CPU wins ======>")
		
	print("Do you want to play again? (Y/N)")
	ans = input()


	
	if ans == 'n' or ans == 'N':
		break
	

print("\nThanks for playing")

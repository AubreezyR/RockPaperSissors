import random
COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0
INVALID = 3
ROCK = 1
PAPER = 2
SCISSORS = 3

def choiceString(choice):
	if choice == 1:
		return "rock"
	elif choice == 2:
		return "paper"
	elif choice == 3:
		return "scissors"
	else:
		return "Something went wrong"

	

def rockPaperScissors(computer,player):
	if computer == "rock" and player == "scissors":
		return COMPUTER_WINS
	elif computer == "rock" and player == "paper":
		return PLAYER_WINS
	elif computer == "paper" and player == "rock":
		return COMPUTER_WINS
	elif computer == "paper" and player =="scissors":
		return PLAYER_WINS
	elif computer == "scissors" and player =="paper":
		return COMPUTER_WINS
	elif computer == "scissors" and player =="rock":
		return PLAYER_WINS
	elif computer == player:
		return TIE
	else:
		return INVALID

	




def main():
	a = True
	while a:
		try:
			result = 0
	#Loop if its a tie aka 0
			while (result == 0):
		#- Ask the user to choose rock, paper, or scissors 
				player = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))
		#Generate a random number between 1 and 3 for the computer.
				computer = random.randint(1,3)
		#Call choiceString to convert number to computers choice
				c_choice = choiceString(computer)
		#Call choiceString to convert number to persons choice
				p_choice = choiceString(player)
		#Call value returning function to get result of game
				result = rockPaperScissors(c_choice,p_choice)
		# print the computer’s hand
				print("Computer chose:", c_choice)
		#print persons hand 
				print("Player chose:", p_choice)
				if result == 0:
			#print message for tie
					print("You made the same choice as the computer. Starting over...")
				elif result == 1:
			#print message for computer win
					print("The computer wins the game")
				elif result == 2:
			#print message for player win
					print("You win the game")
				else:
			#print message for invalid choice
					print("You made an invalid choice. No winner")
		except ValueError:
			print("Error Invalid input. Please input 1 for rock, 2 for paper, or 3 for scissors") 

	

main()

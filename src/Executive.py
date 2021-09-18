import gameBoard.py
import os
clear = lambda: os.system('cls')

class Executive:
	#Class Attributes
	playerTurn = 0		# 0 if player one's turn, 1 if player two's turn
	roundNum = 0		#Keeps track of what round the game is on. Extra, but could be used on transition screen and win screen
	
	#Constructor: Creates two gameBoard instances
	def __init__(self):
		self.boardOne = gameBoard()
		self.boardTwo = gameBoard()

	#Calls upon internal methods in order
	def runGame(self):
	#variable needed to transfer information from self.takeTurn to self.transition - andrew
		turnResult = [0, "A", 0]

		#Ask how many ships there will be
		self.numShips1 = int(input("Player 1: How many ships would you like in your BattleShip game: ")) #I reread the assignment and I definitely think we need one number of ships for both players - Gavin
		self.numShips2 = int(input("Player 2: How many ships would you like in your BattleShip game: "))

		#Set up each player's board
		self.setUp(self.boardOne, self.numShips1)
		self.setUp(self.boardTwo, self.numShips2)

		
		# #Each player takes their turn
		# turnResult = self.takeTurn(self.boardOne, self.boardTwo)

		# display transition turn for player one, if player one has won break out of loop
		#if(self.transitionScreen(turnResult))
		#	break

		#increment the playerTurn
		playerTurn = (playerTurn + 1) % 2

		# turnResult = self.takeTurn(self.boardTwo, self.boardOne)

		# display transition turn for player two, if player two has won break out of loop
		#if(self.transitionScreen(turnResult))
		#	break

		#increment the playerTurn
		playerTurn = (playerTurn + 1) % 2
		# #Loop through above logic until someone wins
		self.winScreen()
		

	#Performs the board setup for one player's board. Ships do not have to be placed in order. Will not let players place ships in an invalid spot
	def setUp(self, gameBoard, numShips):
		ShipNames=["LifeBoat(size=1)", "The Destroyer(size=2)", "Submarine(size=3)", "BattleShip(size=4)", "Carrier(size=5)", "Cruiser(size=6)"]
		orientation = True
		x_coordinates = 0
		alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
		for i in range(numShips):
			print( ShipNames[i] )
			Input_orientation = (input("What orientation would you like(H/V)?: "))
			Input_x_coordinates = (input("Where do you want the Ship to be placed on x-axis(eg.A): "))
			y_coordinates = int(input("Where do you want the Ship to be placed on y-axis(eg.4): "))
			ShipSize = int(i+1)
			if (Input_orientation =='H' or Input_orientation == 'h'):
    				orientation = False
			elif (Input_orientation == 'V' or Input_orientation == 'v'):
    				orientation = True

			#WHY, why does this exist. just submit the input_x_coordinates to the Gameboard!!! - Andrew
			for i in range(0, 9):
    				if(alphabet[i] == Input_x_coordinates):
					     x_coordinates = i+1 
						 
			gameBoard.placeShip(ShipSize, orientation, y_coordinates, x_coordinates)
			gameBoard.printPlayerView()
			print(x_coordinates)
			print(y_coordinates)
			print(orientation)
			print(ShipSize)

	#Shows player their view of both game boards, asks for a row and column, then performs a shot. 
	# ?Returns an array containing [row of shot, column of shot, 0-6 miss/ship hit]?
	def takeTurn(self, playerBoard, opponentBoard):
		pass

	#Displays the result of the last shot (hit/miss, which ship was hit/sunk). If a ship was sunk, check if game has been won. If so, end loop and go to winscreen.
	# If not, ask to give control to next player and wait for confirmation
	def transitionScreen(self, turnResults):
		#ship names variable, for easy output
		ShipNames=["LifeBoat(size=1)", "The Destroyer(size=2)", "Submarine(size=3)", "BattleShip(size=4)", "Carrier(size=5)", "Cruiser(size=6)"]

		#If this is the return variable, and if it is true, then the game ends
		endGame = False

		#clear screen and display the turn
		clear()
		print("The turn is " + self.playerTurn)

		#display where shot
		print("Shot on row " + turnResult[0] + " and col " + turnResult[1])

		#display the result of the last shot, and check if that ship was sunk, and check if the game has been won.
		if(not self.playerTurn):
			if(turnResults[2] != 0):
				print("Hit! You hit a " + ShipNames[turnResults[2]-1])
				if(self.boardTwo.gameLost()):
					endGame = True
			else:
				print("You missed!")
			print("please return control to player 2, input any key when done")
		else:
			if(turnResults[2] != 0):
				print("Hit! You hit a " + ShipNames[turnResults[2]-1])
				if(self.boardOne.gameLost()):
					endGame = True
			else:
				print("You missed!")
			print("please return control to player 1, input any key when done")

		input()

		return endGame

	#Displays both boards and announces the winner
	def winScreen(self):
		#Clear screen and display which player won and on what turn
		clear()
		if self.boardOne.gameLost():
			print("Player One wins on round " + self.roundNum + "!\n")
		elif self.boardTwo.gameLost():
			print("Player Two wins on round " + self.roundNum + "!\n")

		#Display both board states and thank the player
		print("Player One's board:\n")
		self.boardOne.printPlayerView()
		print()
		print("Player Two's board:\n")
		self.boardTwo.printPlayerView()
		print()
		print("Thanks for playing!")
		print("press any button to continue...")
		input()

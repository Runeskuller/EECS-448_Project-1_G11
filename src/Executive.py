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
		#Ask how many ships there will be
		self.numShips = input
		#Set up each player's board
		self.setUp(self.boardOne)
		self.setUp(self.boardTwo)
		#Each player takes their turn
		self.takeTurn(boardOne, boardTwo)
		self.transitionScreen()
		self.takeTurn(boardTwo, boardOne)
		self.transitionScreen()
		#Loop through above logic until someone wins
		self.winScreen()
		

	#Performs the board setup for one player's board. Ships do not have to be placed in order. Will not let players place ships in an invalid spot
	def setUp(self, gameBoard):
		pass

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

		#display the turn
		print("The turn is " + self.playerTurn)

		#display where shot
		print("Shot on row " + turnResult[0] + " and col " + turnResult[1])

		#display the result of the last shot, and check if that ship was sunk, and check if the game has been won.
		if(not self.playerTurn):
			if(turnResults[2] != 0):
				print("Hit! You hit a " + ShipNames[turnResults[2]])
				if(self.boardTwo.gameLost()):
					endGame = True
			else:
				print("You missed!")
			print("please return control to player 1, input any key when done")
		else:
			if(turnResults[2] != 0):
				print("Hit! You hit a " + ShipNames[turnResults[2]])
				if(self.boardOne.gameLost()):
					endGame = True
			else:
				print("You missed!")
			print("please return control to player 1, input any key when done")

		input()

		return endGame

	#Displays both boards and announces the winner
	def winScreen(self):
		pass
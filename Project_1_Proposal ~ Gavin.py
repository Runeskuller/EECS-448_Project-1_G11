

class Executive:
	#Class Attributes
	playerTurn = 1		# 1 if player one's turn, 2 if player two's turn
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
		self.takeTurn(self.boardOne, self.boardTwo)
		self.transitionScreen()
		self.takeTurn(self.boardTwo, self.boardOne)
		self.transitionScreen()
		#Loop through above logic until someone wins
		self.winScreen()
		

	#Performs the board setup for one player's board. Ships do not have to be placed in order. Will not let players place ships in an invalid spot
	def setUp(self, gameBoard):
		ShipNames =["LifeBoat(size=1)", "The Destroyer(size=2)", "Submarine(size=3)", "BattleShip(size=4)", "Carrier(size=5)", "Cruiser(size=6)"]
		for i in self.numShips: 
			print( ShipNames[i] )
			orientation = (input("What orientation would you like(H/V)?: "))
			x_coordinates = (input("Where do you want the Ship to be placed on x-axis(eg.A): "))
			y_coordinates = (input("Where do you want the Ship to be placed on y-axis(eg.4): "))
			ShipSize = int(i)
			gameBoard.placeShip(ShipSize, orientation, y_coordinates, x_coordinates)
				
		

		
		
	#Shows player their view of both game boards, asks for a row and column, then performs a shot. 
	# ?Returns an array containing [row of shot, column of shot, 0-6 miss/ship hit]?
	def takeTurn(self, playerBoard, opponentBoard):
		pass

	#Displays the result of the last shot (hit/miss, which ship was hit/sunk). If a ship was sunk, check if game has been won. If so, end loop and go to winscreen.
	# If not, ask to give control to next player and wait for confirmation
	def transitionScreen(self, turnResults):
		pass

	#Displays both boards and announces the winner
	def winScreen(self):
		pass



class gameBoard:
	#Class Attributes
	columns = 10
	rows = 9
	

	#Constructor: Creates a 2D array of integers with all spots marked empty(0)
	def __init__(self):
		self.board = [[int(0)]*self.columns]*self.rows

	#Places a ship in the grid, represented by a number equal to the size of the ship e.g. a 1x3 ship would be three adjacent 3's on the grid
	def placeShip(self, orientation, row, column, shipSize):
		pass

	#Checks the spot on board, if there is no ship then marks it as a miss(#) and returns 0, if there is a ship then marks as a hit(X) and returns the size of the ship hit
	def shotOn(self, row, column):
		pass

	#Checks the board to see if a specific ship has been sunk. Returns true if no spaces hold the number 'shipSize'. Returns false otherwise
	def shipSunk(self, shipSize):
		pass

	#Checks if any ships are left unsunk, returns true if there are no spaces on the board representing a ship. Returns false otherwise
	def gameLost(self):
		pass

	#Prints the grid, showing ships and hits and misses
	def printPlayerView(self):
		pass

	#Prints the grid, showing only hits and misses
	def printOpponentView(self):
		pass


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
		self.numShips1 = int(input("Player 1: How many ships would you like in your BattleShip game: "))
		self.numShips2 = int(input("Player 2: How many ships would you like in your BattleShip game: "))

		#Set up each player's board
		self.setUp(self.boardOne, self.numShips1)
		self.setUp(self.boardTwo, self.numShips2)
		# #Each player takes their turn
		# self.takeTurn(self.boardOne, self.boardTwo)
		# self.transitionScreen()
		# self.takeTurn(self.boardTwo, self.boardOne)
		# self.transitionScreen()
		# #Loop through above logic until someone wins
		# self.winScreen()
		

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
			y_coordinates = (input("Where do you want the Ship to be placed on y-axis(eg.4): "))
			ShipSize = int(i+1)
			if (Input_orientation =='H' or Input_orientation == 'h'):
    				orientation = False
			elif (Input_orientation == 'V' or Input_orientation == 'v'):
    				orientation = True
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
		pass

	#Displays both boards and announces the winner
	def winScreen(self):
		pass


class gameBoard:
	# Class Attributes
	columns = 10
	rows = 9

	# test change

	# Constructor: Creates a 2D array of integers with all spots marked empty(0)
	def __init__(self):
		self.board = [["0" for i in range(self.columns)]
		                   for j in range(self.rows)]

	# Returns the content of the specified tile
	def getTile(self, row, col):
		return(self.board[row][col])

	# Called when setting up the board. Takes the type of ship, along with the orientation and coordinates for the leftmost or topmost coordinate of the ship.
	def placeShip(self, size, orientation, row, col): #(1, 4, 5, 4)
		success = False
		fail = False
		while not success:
			if orientation:
				if row in range(1,9) and col in range(1, 10):
					if row + size <= 10:
						for i in range(row, row + size):
							if self.board[i-1][col] != "0":
								fail = True

						if fail:
							break

						for i in range(row, row + size):
							if self.board[i-1][col] == "0":
								self.board[i-1][col] = str(size)
								success = True
					else:
						break
				else:
					break

			elif not orientation:
				if row in range(1,9) and col in range(1, 10):
					print("got 1")
					if col + size <= 11:
						print("got 2")
						for i in range(col, col + size):
							if self.board[row-1][i-1] != "0":
								fail = True

						if fail:
							break

						for i in range(col, col + size):
							if self.board[row-1][i-1] == "0":
								self.board[row-1][i-1] = str(size)
								success = True
					else:
						break
				else:
					break
        
    # asserts whether a shot at a given coordinate is a hit or miss
	def shotOn(self, xPos, yPos):
		if(self.board[xPos][yPos] == "2" or self.board[xPos][yPos] == "3" or self.board[xPos][yPos] == "4" or self.board[xPos][yPos] == "5"):
			print("Hit!")
		else:
			print("Miss!")
            # checkIfSunk()

	# Checks the board to see if a specific ship has been sunk. Returns true if no spaces hold the number 'shipSize'. Returns false otherwise
	def shipSunk(self, shipSize):
		sunk = bool(1)
		for i in range(self.rows):
			for j in range(self.columns):
				if self.board[i][j] == shipSize:
					sunk = bool(0)
		return(sunk)

	# Checks if any ships are left unsunk, returns true if there are no spaces on the board representing a ship. Returns false otherwise
	def gameLost(self):
		lost = bool(1)
		for i in range(self.rows):
			for j in range(self.columns):
				if not(self.board[i][j] == 0 or self.board[i][j] == 'X' or self.board[i][j] == '*'):
					lost = bool(0)
		return(lost)

	# Prints the grid, showing ships and hits and misses
	def printPlayerView(self):
		print("   ", end = '')
		for i in range(self.columns):
			char = chr(65+i)
			print(char, " ", end = '')

		print()

		for i in range(self.rows):
			print(i+1, " ", end = '')
			for j in range(self.columns):
				print(self.board[i][j], " ", end = '')
			print()

	# Prints the grid, showing only hits and misses
	def printOpponentView(self):
		print("   ", end = '')
		for i in range(self.columns):
			char = chr(65+i)
			print(char, " ", end = '')

		print()

		for i in range(self.rows):
			print(i+1, " ", end = '')
			for j in range(self.columns):
				if self.board[i][j] == 'X' or self.board[i][j] == '*':
					print(self.board[i][j], " ", end = '')
				else:
					print('0', " ", end = '')
			print()


Exec = Executive()
Exec.runGame()

grid1 = gameBoard()
grid1.printPlayerView()
print(grid1.getTile(1,5))

grid1.shotOn(0,4)
grid1.placeShip(5, 1, 6, 7)
grid1.placeShip(4, 1, 6, 7)
grid1.printPlayerView()
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
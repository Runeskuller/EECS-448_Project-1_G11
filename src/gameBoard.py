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
	def placeShip(self, size, orientation, row, col): #i.e. (4, True, 5, 4)
		success = False  #this flag used to end while loop without breaking
		fail = False     #this flag used to break the loop and return a negative result if the input would lead to invalid placement
		while not success:
			#vertical
			if orientation:
				if row + size <= 10:
					for i in range(row, row + size):
						if self.board[i-1][col-1] != "0": #dry run checking if there are any ships in the way of placement
							fail = True

					if fail:
						break

					for i in range(row, row + size):
						if self.board[i-1][col-1] == "0":
							self.board[i-1][col-1] = str(size)  #placing ship
							success = True
				else:
					fail = True
					break

			#horizontal
			elif not orientation:
				if col + size <= 11:
					for i in range(col, col + size):
						if self.board[row-1][i-1] != "0": #dry run checking if there are any ships in the way of placement
							fail = True

					if fail:
						break

					for i in range(col, col + size):
						if self.board[row-1][i-1] == "0":
							self.board[row-1][i-1] = str(size)  #placing ship
							success = True
				else:
					fail = True
					break
		return(fail)

    # asserts whether a shot at a given coordinate is a hit or miss
	def shotOn(self, row, col):
		if(self.board[row][col] == "0"):
			self.board[row][col] = '*'
			return(0)
		elif(self.board[row][col] == '*' or self.board[row][col] == "X"):
			return(0)
		else:
			size = int(self.board[row][col])
			self.board[row][col] = 'X'
			return(size)

	# Checks the board to see if a specific ship has been sunk. Returns true if no spaces hold the number 'shipSize'. Returns false otherwise
	def shipSunk(self, shipSize):
		sunk = False
		for i in range(self.rows):
			for j in range(self.columns):
				if self.board[i][j] == shipSize:
					sunk = True
		return(sunk)

	# Checks if any ships are left unsunk, returns true if there are no spaces on the board representing a ship. Returns false otherwise
	def gameLost(self):
		lost = bool(1)
		for i in range(self.rows):
			for j in range(self.columns):
				if not(self.board[i][j] == "0" or self.board[i][j] == 'X' or self.board[i][j] == '*'):
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
				if self.board[i][j] == "0":
					print("~", " ", end = '')
				else:
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
					print('~', " ", end = '')
			print()
'''
	Andres Schuchert
	CS 5001
	December 2, 2018
'''
import graphics
import random
import file

class Board:

	def __init__(self,size=4):
		'''
		Intialize values
		'''
		self.size = size
		self.game_board = []
		self.move = "black"

	def __str__(self):
		'''
		Make the board printable
		'''
		return str(self.game_board)

	def __eq__(self,size):
		if self.size == size:
			return True
		else:
			return False
	def is_valid_size(self,size):
		'''
		Function name: is_valid_size
		Parameters: int
		Return: boolean
		Description: returns a valid size
		'''
		if size >= 4 and size % 2 == 0:
			return True
		else:
			return False

	def is_valid_point(self,x,y):
		'''
		Function name: is_valid_point
		Parameters: int, int
		Return: boolean
		Description: Determines if a point is a valid point on the board.
		'''
		try:
			if not str(x).isidentifier() and not str(y).isidentifier():

				if abs(x) < (self.size * 25) and abs(y) < (self.size * 25):
					return True
				else:
					return False
			else:
				print("Error: Function parameters do not allow booleans")
				return False

		except TypeError:
			print("Error: Function parameters do not allow strings.")
			return False

	def is_out_of_bounds(self,row,col):
		'''
		Function Name: is_out_of_bounds
		Parameters: int, int
		Return: Boolean
		Description: If row or col are invalid indicies return true, otherwise
		false
		'''
		if row < 0 or col < 0:
			return True
		elif row >= self.size or col >= self.size:
			return True
		else: 
			return False
	
	def is_adjacent(self,row,col):
		'''
		Functiona Name: is_adjacent
		Parameters: int, int
		Return: boolean
		Description: If index is out of bounds or if stone is adjacent to same
		type return true, otherwise return false
		'''
		if not self.is_out_of_bounds(row,col):
			if self.game_board[row][col] == self.check_stone():
				return True
			else:
				return False
		else:
			return True

	def is_cell_empty(self, row, col):
		'''
		Function name: is_cell_empty
		Parameters: list of list, int, int
		Return: boolean
		Description: If board spot is empty return true, otherwise false
		'''
		if not self.is_out_of_bounds(row,col):
			if self.game_board[row][col] == 0:
				return True
			else:
				return False
		else: 
			return False
	def is_board_full(self,n,board):
		'''
		Function name: is_board_full
		Parameters: int, list of lists
		Return: boolean
		Description: Returns true if no 0s are found, otherwise false
		'''
		for i in range(n):
			if 0 in board[i]:
				return False
		return True

	def calculate_stone_position(self,n):
		'''
		Function name: calculate_stone_position
		Parameters: int
		Return: list
		Description: Calculate starting stones' position
		'''
		col = n // 2
		row = n // 2
		stone_pos = [[row - 1,col-1],[row - 1,col],[row,col],[row,col-1]]
		return stone_pos

	def calculate_midpoint(self, rows, cols):
		'''
		Function name: calculate_midpoint
		Parameters: int, int
		Return: list
		Description: Calculates the midpoint for the circle drawing
		FLOATS WILL BREAK IT, IF GIVEN
		'''
		try:
			if not str(rows).isidentifier() and not str(cols).isidentifier():
				temp_x = (cols * 50) + 25
				temp_y = (rows * 50) + 50
				x_mid = temp_x - (self.size * 25)
				y_mid = -temp_y + (self.size * 25)
				return [x_mid,y_mid]
			else:
				return []
		except TypeError:
			print("Error: Function parameters do not allow strings.")
			return []

	def count_stones(self,n,board):
		'''
		Function name: count_stones
		Parameters: int, list of lists 
		Return: list
		Description: Return a list containing the number of black stones,
		represented with 1, and white stones, represented with -1.
		'''
		black = 0
		white = 0

		for i in range(n):
			for j in range(n):
				if board[i][j] == 1:
					black += 1
				else:
					white += 1
		return [black,white]

	def determine_spot(self,x,y):
		'''
		Function name: determine_spot
		Parameters: int, int
		Return: list
		Description: Determines the positon by point value
		'''
		if self.is_valid_point(x,y):
			x = (self.size * 25) + x
			column = x // 50
			y = (self.size * 25) - y
			row = y // 50
			return [int(row),int(column)]
		else:
			return []

	def determine_winner(self, n,board):
		'''
		Function name: determine_winner
		Parameters: int, list of lists
		Return: Player stones
		Description: Determines the winner of the game
		'''

		num_stones = self.count_stones(n,board)
		if num_stones[0] > num_stones[1]:
			print("Black stones: " + str(num_stones[0]))
			print("White stones: " + str(num_stones[1]))
			print("BLACK WINS")
		elif num_stones[0] < num_stones[1]:
			print("Black stones: " + str(num_stones[0]))
			print("White stones: " + str(num_stones[1]))
			print("WHITE WINS")
		else:
			print("Black stones: " + str(num_stones[0]))
			print("White stones: " + str(num_stones[1]))
			print("TIE!!!")
		return num_stones[0]
	def set_size(self,size):
		'''
		Function name: set_size
		Parameters: int
		Return: boolean
		Description: Set the size of the game board
		'''
		if self.is_valid_size(size):
			self.size = size
		else:
			print("Error: Invalid board size. Default setting applied")
			self.size = 4

	def get_size(self):
		''' 
		Function name: get_size
		Parameters: none
		Return: int
		Description: Returns the size of the board
		'''
		return self.size
	
	def initialize_board(self):
		'''
		Function name: initialize_board
		Parameters: none
		Return: none
		Description: Initialize board to store stones. Empty spots are
		give the value 0
		'''
		for i in range(self.size):
			cols = []
			for j in range(self.size):
				cols.append(0)
			self.game_board.append(cols)

	def initialize_stones(self,n):
		'''
		Function name: initialize_stones
		Parameters: int
		Return: None
		Description: Set four starter stones in the center
		'''
		stone_pos = self.calculate_stone_position(n)
		midpoints = []
		for i in range(len(stone_pos)):
			midpoint = self.calculate_midpoint(stone_pos[i][0],stone_pos[i][1])
			midpoints.append(midpoint)
		for i in range(len(stone_pos)):
			self.update_board(stone_pos[i][0],stone_pos[i][1])
			graphics.draw_stone(midpoints[i],self.move)
			self.update_move()

	def update_board(self,row,col):
		'''
		Function name: update_board
		Parameters: list of lists, int, int
		Return: None
		Description: Update the value in a board spot
		'''
		if self.move == "black":
			self.game_board[row][col] = 1
		else:
			self.game_board[row][col] = -1

	def update_move(self):
		'''
		Function name: update_move
		Parameters: None
		Return: None
		Description: Update the move
		'''
		if self.move == "black":
			self.move = "white"
		else:
			self.move = "black"

	def check_stone(self):
		'''
		Function name: check_stone
		Parameters: None
		Return: Int
		Description: Return an integer value of the stone color
		'''
		if self.move == "black":
			return 1
		else:
			return -1

	def check_left_row(self, row, col):
		'''
		Function name: check_left_row
		Parameters: int, int
		Return: Boolean
		Description: Check if there is a same color stone on the leftside
		row without being adjacent to one or an empty space
		'''
		col -= 1
		if not self.is_adjacent(row,col):
			while col >= 0:
				if self.game_board[row][col] == self.check_stone():
					return True
				elif self.game_board[row][col] == 0:
					return False
				else:
					col -= 1
			return False
		else:
			return False
	def check_right_row(self, row, col):
		'''
		Function name: check_right_row
		Parameters: int, int
		Return: Boolean
		Description: Check if there is a same color stone on the rightside
		row without being adjacent to one or an empty space
		'''
		col += 1
		if not self.is_adjacent(row,col):
			while col < self.size:
				if self.game_board[row][col] == self.check_stone():
					return True
				elif self.game_board[row][col] == 0:
					return False
				else:
					col += 1
			return False
		else:
			return False
	def check_top_column(self, row, col):
		'''
		Function name: check_top_column
		Parameters: int, int
		Return: Boolean
		Description: Check if there is a same color stone on the top column
		without being adjacent to one or an empty space
		'''
		row -= 1
		if not self.is_adjacent(row,col):
			while row >= 0:
				if self.game_board[row][col] == self.check_stone():
					return True
				elif self.game_board[row][col] == 0:
					return False
				else:
					row -= 1
			return False
		else:
			return False

	def check_bottom_column(self, row, col):
		'''
		Function name: check_bottom_column
		Parameters: int, int
		Return: Boolean
		Description: Check if there is a same color stone on the bottom column
		without being adjacent to one or an empty space
		'''
		row += 1
		if not self.is_adjacent(row,col):
			while row < self.size:
				if self.game_board[row][col] == self.check_stone():
					return True
				elif self.game_board[row][col] == 0:
					return False
				else:
					row += 1
			return False
		else:
			return False

	def check_top_backslash(self, row, col):
		'''
		Function name: check_top_backslash
		Parameters: int, int
		Return: Boolean
		Description: Check if there is a same color stone on the upward 
		backslash without being adjacent to one or an empty space
		'''
		row -= 1
		col -= 1
		if not self.is_adjacent(row,col):
			while row >= 0 and col >= 0:
				if self.game_board[row][col] == self.check_stone():
					return True
				elif self.game_board[row][col] == 0:
					return False
				else:
					row -= 1
					col -= 1
			return False
		else:
			return False
	def check_bottom_backslash(self,row,col):
		'''
		Function name: check_bottom_backslash
		Parameters: int, int
		Return: Boolean
		Description: Check if there is a same color stone on the downward 
		backslash without being adjacent to one or an empty space
		'''
		row += 1
		col += 1
		if not self.is_adjacent(row,col):
			while row < self.size and col < self.size:
				if self.game_board[row][col] == self.check_stone():
					return True
				elif self.game_board[row][col] == 0:
					return False
				else:
					row += 1
					col += 1
			return False
		else:
			return False
	def check_top_forwardslash(self, row, col):
		'''
		Function name: check_forwardslash
		Parameters: int, int
		Return: Boolean
		Description: Check if there is a same color stone on the upward 
		forwardslash without being adjacent to one or an empty space
		'''
		row -= 1
		col += 1
		if not self.is_adjacent(row,col):
			while row >= 0 and col < self.size:
				if self.game_board[row][col] == self.check_stone():
					return True
				elif self.game_board[row][col] == 0:
					return False
				else:
					row -= 1
					col += 1
			return False
		else:
			return False
	def check_bottom_forwardslash(self, row, col):
		'''
		Function name: check_bottom_forwardslash
		Parameters: int, int
		Return: Boolean
		Description: Check if there is a same color stone on the downward 
		forwardslash without being adjacent to one or an empty space
		'''
		row += 1
		col -= 1
		if not self.is_adjacent(row,col):
			while row < self.size and col >= 0:
				if self.game_board[row][col] == self.check_stone():
					return True
				elif self.game_board[row][col] == 0:
					return False
				else:
					row += 1
					col -= 1
			return False
		else:
			return False
	def check_backslash(self,row,col):
		'''
		Function name: check_backslash
		Paramters: int, int
		Return: Boolean
		Description: Check if  backslash is a valid move
		'''
		if self.check_top_backslash(row,col) or self.check_bottom_backslash(row,col):
			return True
		else:
			return False

	def check_forwardslash(self,row,col):
		'''
		Function name: check_backslash
		Paramters: int, int
		Return: Boolean
		Description: Check if forwardslash is a valid move
		'''
		if self.check_top_forwardslash(row,col) or self.check_bottom_forwardslash(row,col):
			return True
		else:
			return False

	def check_col(self, row, col):
		'''
		Function name: check_backslash
		Paramters: int, int
		Return: Boolean
		Description: Check if column is a valid move
		'''
		if self.check_top_column(row,col) or self.check_bottom_column(row,col):
			return True
		else:
			return False

	def check_row(self, row, col):
		'''
		Function name: check_backslash
		Paramters: int, int
		Return: Boolean
		Description: Check if row is a valid move
		'''
		if self.check_left_row(row,col) or self.check_right_row(row,col):
			return True
		else:
			return False

	def check_legal_move(self,cell):
		'''
		Function name: check_leagal_move
		Paramters: list
		Return: Boolean
		Description: Determine if a cell is a possible legal move for a stone
		'''
		if self.check_row(cell[0],cell[1]) or\
			self.check_col(cell[0],cell[1]) or\
			self.check_backslash(cell[0],cell[1]) or\
			self.check_forwardslash(cell[0],cell[1]):
			return True
		return False

	def flip_col_stones(self, row, col, direction):
		'''
		Function name: flip_col_stones
		Paramters: int,int,int
		Return: None
		Description: Flips stones in columns based on the direction. The
		direction is determined by even or odd. An even integer will flip
		stones left and odd will flip stones right
		'''
		while self.game_board[row][col] != self.check_stone():
			self.update_board(row,col)
			midpoint = self.calculate_midpoint(row,col)
			graphics.draw_stone(midpoint, self.move)
			if direction % 2 == 0:
				col -= 1
			else:
				col += 1
	def flip_row_stones(self,row,col,direction):
		'''
		Function name: flip_row_Stones
		Paramters: int,int,int
		Return: None
		Description: Flips stones in row based on the direction. The
		direction is determined by even or odd. An even integer will flip
		stones upward and odd will flip stones downward
		'''
		while self.game_board[row][col] != self.check_stone():
			self.update_board(row,col)
			midpoint = self.calculate_midpoint(row,col)
			graphics.draw_stone(midpoint,self.move)
			if direction % 2 == 0:
				row -= 1
			else:
				row += 1
	def flip_backslash(self, row, col,direction):
		'''
		Function name: flip_backslash
		Paramters: int,int,int
		Return: None
		Description: Flips stones in backslash diagonal based on the direction. 
		The direction is determined by even or odd. An even integer will flip
		stones upward and odd will flip stones downward
		'''
		while self.game_board[row][col] != self.check_stone():
			self.update_board(row,col)
			midpoint = self.calculate_midpoint(row,col)
			graphics.draw_stone(midpoint,self.move)
			if direction % 2 == 0:
				row -= 1
				col -= 1
			else:
				row += 1
				col += 1
	def flip_forwardslash(self,row,col,direction):
		'''
		Function name: flip_forwardslash
		Paramters: int,int,int
		Return: None
		Description: Flips stones in forward slash diagonal based on the 
		direction. The direction is determined by even or odd. An even integer
		will flip stones upward and odd will flip stones downward
		'''
		while self.game_board[row][col] != self.check_stone():
			self.update_board(row,col)
			midpoint = self.calculate_midpoint(row,col)
			graphics.draw_stone(midpoint,self.move)
			if direction % 2 == 0:
				row -= 1
				col += 1
			else:
				row += 1
				col -= 1

	def flip_stones(self, stone):
		'''
		Function name: flip_stones
		Parameters: stone
		Return: None
		Description: Flip stones in any direction that is considered valid
		'''
		#ROWS
		if self.check_left_row(stone[0],stone[1]):
			self.flip_col_stones(stone[0],stone[1]-1,0)
		if self.check_right_row(stone[0],stone[1]):
			self.flip_col_stones(stone[0],stone[1]+1,1)

		#COLUMNS
		if self.check_top_column(stone[0], stone[1]):
			self.flip_row_stones(stone[0]-1,stone[1],0)
		if self.check_bottom_column(stone[0],stone[1]):
			self.flip_row_stones(stone[0]+1,stone[1],1)

		#BACKWORD SLASH
		if self.check_top_backslash(stone[0],stone[1]):
			self.flip_backslash(stone[0]-1,stone[1]-1,0)
		if self.check_bottom_backslash(stone[0],stone[1]):
			self.flip_backslash(stone[0]+1,stone[1]+1,1)

		#FORWARD SLASH
		if self.check_top_forwardslash(stone[0],stone[1]):
			self.flip_forwardslash(stone[0]-1,stone[1]+1,0)
		if self.check_bottom_forwardslash(stone[0],stone[1]):
			self.flip_forwardslash(stone[0]+1,stone[1]-1,1)

	def scan_board(self):
		'''
		Function name: scan_board
		Parameters: None
		Return: List of lists
		Description: Determine all possible empty cells that could hold a 
		stone. Does not allow duplicates
		'''
		possible_moves = []
		for i in range(self.size):
			for j in range(self.size):
				if not self.is_cell_empty(i,j):
					moves = self.scan_around_cell(i,j)
					for k in range(len(moves)):
						if moves[k] not in possible_moves:
							possible_moves.append(moves[k])				
		return possible_moves

	def scan_around_cell(self, row, col):
		'''
		Funcation name: scan_around_cell
		Parameters: int, int
		Return: List
		Description: Scan in all directions by one cell and append to list
		if cell is empty. 
		'''	
		moves = []
		#Right
		if self.is_cell_empty(row, col+1):
			moves.append([row,col+1])
		#Left
		if self.is_cell_empty(row, col-1):
			moves.append([row,col-1])
		#Up
		if self.is_cell_empty(row+1, col):
			moves.append([row+1,col])
		#Down
		if self.is_cell_empty(row-1, col):
			moves.append([row-1,col])
		#Backslash downwards
		if self.is_cell_empty(row+1, col+1):
			moves.append([row+1,col+1])
		#Backslash upwards
		if self.is_cell_empty(row-1, col-1):
			moves.append([row-1,col-1])
		#Forwardslash upwards
		if self.is_cell_empty(row-1, col+1):
			moves.append([row-1,col+1])
		#Forwardslash downwards
		if self.is_cell_empty(row+1, col-1):
			moves.append([row+1,col-1])
		return moves

	def clicked(self,x,y):
		'''
		Function name: clicked
		Parameters: int, int
		Return: None
		Description: 
		'''
		graphics.screen_goto(x,y)
		spot = self.determine_spot(x,y)
		both_legal_moves = []
		if len(spot) != 0:
			midpoint = self.calculate_midpoint(spot[0],spot[1])
			possible_moves = self.scan_board()
			player_legal_moves = []
			for i in range(len(possible_moves)):
					if self.check_legal_move(possible_moves[i]):
						player_legal_moves.append(possible_moves[i])
			print("Player Possible Moves: " + str(possible_moves))
			if self.is_cell_empty(spot[0],spot[1]):
				if self.check_legal_move(spot):
					self.update_board(spot[0],spot[1])
					graphics.draw_stone(midpoint,self.move)
					self.flip_stones(spot)
					self.update_move()
				if len(player_legal_moves) == 0:
					both_legal_moves.append(0)
					self.update_move()
			#################################################################
			#								AI								#
			#################################################################
			if self.move == "white":
				legal_moves = []
				possible_moves = self.scan_board()
				for i in range(len(possible_moves)):
					if self.check_legal_move(possible_moves[i]):
						legal_moves.append(possible_moves[i])
				if len(legal_moves) != 0:
					comp_move = legal_moves[random.randint(0,len(legal_moves)-1)]
					comp_midpoint = self.calculate_midpoint(comp_move[0], comp_move[1])
					self.update_board(comp_move[0],comp_move[1])
					graphics.draw_stone(comp_midpoint,self.move)
					self.flip_stones(comp_move)
					self.update_move()
				else:
					both_legal_moves.append(0)
					self.update_move()
			
			#################################################################
			#							GAME ENDS							#
			#################################################################
			if self.is_board_full(self.size,self.game_board) or\
				(len(legal_moves) == 0 and len(player_legal_moves) == 0):
				print("GAME IS OVER")
				player_stones = self.determine_winner(self.size,self.game_board)
				username = input("Enter your username: ")
				users = file.read_users("scores.txt")
				#Need to set a value for wins
				if file.is_empty(users):
					file.add_user("scores.txt", username, player_stones)
				else:
					file.determine_highscore("scores.txt",users, 
						username, player_stones)

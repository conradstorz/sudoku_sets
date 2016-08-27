# sudoku.py

""" routines that will implement a solver for Sudoku puzzles.
	"""

class game_cell(object):
	""" the basic element of the game
		"""

	def __init__(self, n):
		""" initiate an individual game cell with the n number of elements
			"""
		self.cell = set(range(n))

	def is_solved(self):
		""" return true if cell contains only one element
			"""
		return len(self.cell) == 1



class game_board(object):
	""" the collection of game_cells that comprise the game
		"""

	def __init__(self, board_size):
		""" initiate game board
			"""

	def is_solved(self):
		""" return true if game is solved
			"""




def build_the_game():
	""" create the elements of a complet game
		"""


def load_a_saved_game():
	""" read a partially solved game from premanent storage
		"""


def display_the_board():
	""" put the current game board on the screen
		"""



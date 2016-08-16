# sudoku_sets

This is an attempt to implement a sudoku solver. 
My plan is to use sets to track and solve the puzzle.
Starting position files may be entered as a list of lists, 
	a list of strings, or possibly other forms.
The "blank" positions in the puzzle can be represented by 
	ANY character not in the VALID set of characters.

The data structure will be an array of sets. 
Each set will include all available elements. 
Array elements that have been declared (solved)
	at the start will contain only one (1) element. 
Blank spaces in the puzzle (unsolved) will contain 
	all of the possible elements available.


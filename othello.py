'''
	Andres Schuchert
	CS 5001
	December 2, 2018
'''
from board import Board
import graphics

def main():
	b = Board(8)
	b.initialize_board()
	graphics.draw_board(b.get_size())
	b.initialize_stones(b.get_size())
	#Run program
	graphics.screen_click(b.clicked)
	#Keep board open
	graphics.keep_board_open()

main()

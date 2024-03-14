#!/usr/bin/python3

from board import Board
from menu import Menu
from player import Player
import os
import time

class Game:

    def __init__(self):
        self.board = Board()
        self.players = [Player(), Player()]
        self.menu = Menu()
        self.current_player = 0

    def start_game(self):
        Game.loading_screen()
        choice = self.menu.display_main_menu()
        if choice == 'S':
            self.setup_players()
            Game.loading_screen()
            self.play_game()
        elif choice == 'Q':
            self.quit_game()
        else:
            print("Invalid Choice!")
        
    def setup_players(self):
        for player in self.players:
            player.choose_name()
            player.choose_symbol()

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                Game.clear_screen()
                self.board.display_board()
                index = 1 - self.current_player
                if self.check_win():
                    print('\033[93m' + f"     *** {self.players[index].name} wins! ***" + '\033[0m')
                elif self.check_draw():
                    print('\033[91m' + "Game Over!" + '\033[0m')
                time.sleep(1)
                choice = self.menu.display_endgame_menu()
                if choice == 'R':
                    self.restart_game()
                elif choice == 'Q':
                    self.quit_game()
                    break
                else:
                    print("Invalid choice")
            Game.clear_screen()
            
                

    def play_turn(self):
        player = self.players[self.current_player]
        self.board.display_board()
        print(f"{player.name} turn.")
        while True:
            try:
                choice = int(input("Choose a cell ==> "))
                if self.board.update_board(choice, player.symbol):
                    break
                print("Invalid move! Try agin.")
            except ValueError:
                print("Please Enter a number.")
        self.switch_player()

    def switch_player(self):
        self.current_player = 1 - self.current_player

    def check_win(self):
        win_com = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], #Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], #Column
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in win_com:
            if (self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                return True
        return False

    def check_draw(self):
        all(not cell.isdigit for cell in self.board.board)

    def restart_game(self):
        self.board.reset_board()
        self.current_player = 0
        self.start_game()

    def quit_game(self):
        Game.clear_screen()
        print("Thank you for playing!")

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def loading_screen():
        print("Loading...")
        time.sleep(1)
        Game.clear_screen()


game = Game()
game.start_game()
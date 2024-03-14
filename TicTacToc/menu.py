#!/usr/bin/python3

class Menu:

    def display_main_menu(self):
        print("     ======= Tic-Tac-Toe ======= \n")
        print("Welcom to X - O Game!\n")
        choice = input("S- to start the game \nQ- to quit the game \n> ")
        return choice

    def display_endgame_menu(self):
        choice = input("Type R to restart the game and Q to quit: ")
        return choice
            
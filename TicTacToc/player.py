#!/usr/bin/python3

class Player:

    def __init__(self):
        self.name = ''
        self.symbol = ''

    def choose_name(self):
        while True:
            name = input("Enter your name: ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name, Letters only.")

    def choose_symbol(self):
        while True:
            symbol = input("Choose your symbol(X or O): ")
            if symbol == 'X':
                self.symbol = '\033[91m' + symbol + '\033[0m'
                break
            elif symbol == 'O':
                self.symbol = '\033[92m' + symbol + '\033[0m'
                break
            print("Invalid symbol, chosse X or O.")
            
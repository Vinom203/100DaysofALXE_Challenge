class Board:

    def __init__(self):
        self.board = [Board.add_color(str(i), 'cayn') for i in range(1,10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print(Board.add_color("|", 'blue').join(self.board[i:i+3]))
            print(Board.add_color("-"*5, 'blue'))

    def update_board(self, index, symbol):
        index -= 1
        if self.is_valid_move(index):
            self.board[index] = symbol
            return True
        return False
            
    def is_valid_move(self, index):
        if index < 0 or index > 8:
            return False
        elif self.board[index] in ['X', 'O']:
            return False
        return True

    def reset_board(self):
        self.board = [str(i) for i in range(1,10)]

    def add_color(text, color):
        colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'purple': '\033[95m',
            'cayn': '\033[96m'
        }
        end_color = '\033[0m'
        if color in colors:
            return (colors[color] + text + end_color)

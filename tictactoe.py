import random


class TicTacToe:
    def __init__(self):
        self.game_board = self.make_new_game_board()
        self.possible_moves = self.generate_all_legal_moves()
        self.player_turn = True
        self.game_tie = False

    def make_new_game_board(self):
        board = []
        for x in range(0, 3):
            row = []
            for y in range(0, 3):
                row.append('_')
            board.append(row)
        return board

    def generate_all_legal_moves(self):
        all_moves_list = []
        for x in range(0, 3):
            for y in range(0, 3):
                all_moves_list.append((x, y))
        return all_moves_list

    def print_game_board(self):
        for row in self.game_board:
            print(" ".join(row))

    def game_loop(self):
        while not self.game_over() and not self.game_tied():
            if self.player_turn:
                print("player turn")
                player_coordinates = self.get_user_coordinates(self.player_turn)
                self.update_game_state(player_coordinates, 'x')
                self.player_turn = False
            else:
                print("computer turn")
                computer_coordinates = self.get_user_coordinates(self.player_turn)
                self.update_game_state(computer_coordinates, 'o')
                self.player_turn = True
            self.print_game_board()

            if self.game_over():
                if not self.player_turn:
                    print('You win')
                else:
                    print('Computer wins')
            elif self.game_tied():
                print('The game is a tie.')

    def get_user_coordinates(self, is_human):
        if is_human:
            while True:
                coordinate_list = input('What is your move?\n').split(',')
                coordinate_tuple = (int(coordinate_list[0]), int(coordinate_list[1]))
                if coordinate_tuple in self.possible_moves:
                    return coordinate_tuple
                else:
                    print('illegal move, pick again')
        else:
            coordinate_list = random.choice(self.possible_moves)
            coordinate_tuple = (int(coordinate_list[0]), int(coordinate_list[1]))
            return coordinate_tuple

    def update_game_state(self, coordinates, marker):
        self.game_board[coordinates[0]][coordinates[1]] = marker
        self.possible_moves.remove(coordinates)

    def game_tied(self):
        if len(self.possible_moves) < 1:
            return True

    def game_over(self):
        # check rows
        for row in self.game_board:
            if len(set(row)) == 1 and '_' not in row:
                return True
        # check columns
        for x in range(len(self.game_board)):
            column = [row[x] for row in self.game_board]
            if len(set(column)) == 1 and '_' not in column:
                return True
        # check diagonals
        diagonal_1 = [self.game_board[x][x] for x in range(len(self.game_board))]
        diagonal_2 = [self.game_board[x][len(self.game_board)-x-1] for x in range(len(self.game_board))]
        if (len(set(diagonal_1)) == 1 and '_' not in diagonal_1) or (len(set(diagonal_2)) == 1 and '_' not in diagonal_2):
            return True



game = TicTacToe()
game.game_loop()


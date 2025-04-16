class Player:
    def __init__(self, name, player_number):
        self.name = name
        self.player_number = player_number

class Ayoayo:
    def __init__(self):
        self.__board = [4] * 6 + [0] + [4] * 6 + [0]
        self.__player1 = None
        self.__player2 = None
        self.__game_ended = False

    def create_player(self, name):
        if self.__player1 is None:
            self.__player1 = Player(name, 1)
            return self.__player1
        elif self.__player2 is None:
            self.__player2 = Player(name, 2)
            return self.__player2
        return None

    def print_board(self):
        print("player1:")
        print(f"store: {self.__board[6]}")
        print(f"{self.__board[:6]}\n")
        
        print("player2:")
        print(f"store: {self.__board[13]}")
        print(f"{self.__board[7:13]}")

    def return_winner(self):
        if not self.__game_ended:
            return "Game has not ended"
        
        p1_score = self.__board[6]
        p2_score = self.__board[13]
        
        if p1_score > p2_score:
            return f"Winner is player 1: {self.__player1.name}"
        elif p2_score > p1_score:
            return f"Winner is player 2: {self.__player2.name}"
        else:
            return "It's a tie"

    def play_game(self, player_index, pit_index):
        if self.__game_ended:
            return "Game is ended"
        
        if pit_index <= 0 or pit_index > 6:
            return "Invalid number for pit index"
        
        current_pit = (pit_index - 1) if player_index == 1 else (pit_index + 6)
        
        if self.__board[current_pit] == 0:
            return "Invalid move - pit is empty"
        
        extra_turn = self._perform_move(player_index, current_pit)
        self._check_game_end()
        
        if extra_turn and not self.__game_ended:
            print(f"player {player_index} take another turn")
        
        return self._get_board_state()

    def _perform_move(self, player_index, current_pit):
        seeds = self.__board[current_pit]
        self.__board[current_pit] = 0
        last_pit = current_pit
        
        while seeds > 0:
            current_pit = (current_pit + 1) % 14
            
            
            if (player_index == 1 and current_pit == 13) or (player_index == 2 and current_pit == 6):
                continue
            
            self.__board[current_pit] += 1
            seeds -= 1
            last_pit = current_pit
        
        extra_turn = False
        
        
        if (player_index == 1 and last_pit == 6) or (player_index == 2 and last_pit == 13):
            extra_turn = True
        
        # Special Rule 2: Capture opponent's seeds
        if not extra_turn:
            player_store = 6 if player_index == 1 else 13
            
            # If last seed was placed in player's own empty pit
            if ((player_index == 1 and 0 <= last_pit <= 5 and self.__board[last_pit] == 1) or
                (player_index == 2 and 7 <= last_pit <= 12 and self.__board[last_pit] == 1)):
                
                opposite_pit = 12 - last_pit
                if self.__board[opposite_pit] > 0:
                    # Capture seeds
                    self.__board[player_store] += self.__board[opposite_pit] + 1
                    self.__board[opposite_pit] = 0
                    self.__board[last_pit] = 0
        
        return extra_turn

    def _check_game_end(self):
        # Check if player 1 has no seeds in their pits
        p1_empty = all(seed == 0 for seed in self.__board[:6])
        
        # Check if player 2 has no seeds in their pits
        p2_empty = all(seed == 0 for seed in self.__board[7:13])
        
        if p1_empty or p2_empty:
            self.__game_ended = True
            
            # Collect remaining seeds
            if p1_empty:
                self.__board[13] += sum(self.__board[7:13])
                for i in range(7, 13):
                    self.__board[i] = 0
            else:
                self.__board[6] += sum(self.__board[:6])
                for i in range(6):
                    self.__board[i] = 0

    def _get_board_state(self):
        return self.__board.copy()
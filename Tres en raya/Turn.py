class Turn:
    def __init__(self, players):
        self.players = list(players.values())
        self.current_turn_index = 0

    def get_current_player(self):
        return self.players[self.current_turn_index]

    def next_turn(self):
        self.current_turn_index = (self.current_turn_index + 1) % len(self.players)
        return self.get_current_player()

    def previous_turn(self):
        self.current_turn_index = (self.current_turn_index - 1) % len(self.players)
        return self.get_current_player()
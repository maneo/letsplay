
class MovesSequence:
    # default_move = 2   # if doubt shoot!
    default_move = 3

    def __init__(self, generation, path_to_evolution):
        self.path_to_evolution = path_to_evolution
        file_with_seq = self.path_to_evolution + "gen_" + str(generation) + ".seq"
        with open(file_with_seq, 'r') as seq_file:
            self.moves = seq_file.readlines()
        self.current_move_idx = 0
        self.generation = generation
        self.seq_is_over = False
        self.done_moves = []

    def next(self):
        if self.current_move_idx < (len(self.moves) - 1):
            current_action = int(self.moves[self.current_move_idx])
            self.done_moves.append(current_action)
            self.current_move_idx = self.current_move_idx + 1
            return current_action
        else:
            # give some time to bullets to reach target
            how_far_beyond = self.current_move_idx - len(self.moves)
            if how_far_beyond > 100:
                self.seq_is_over = True

            current_action = MovesSequence.default_move
            self.done_moves.append(current_action)
            self.current_move_idx = self.current_move_idx + 1
            return current_action

    def save_done_moves(self, score, time, generation, survived):
        file_with_seq = self.path_to_evolution + "gen_" \
                        + str(generation) + "_dead_s_" + str(int(score)) \
                        + "_t_" + str(int(time)) + "_alive_" \
                        + str(int(survived)) + ".seq"
        with open(file_with_seq, 'w') as seq_file:
            for move in self.done_moves:
                seq_file.write(str(move) + "\n")


class GameState:
    frames_to_remember = 2

    def __init__(self, player_vector_size, mob_vector_size, mob_size):
        self.states = list()
        self.player_vector_size = 1  #player_vector_size
        self.mob_vector_size = 48 #mob_vector_size
        self.mob_size = mob_size
        additional_features = 0
        labels_length = 1
        self.state_length = self.player_vector_size + self.mob_vector_size \
                            + additional_features + labels_length

    def __save_game_state(self, current_game_state):
        if len(self.states) == GameState.frames_to_remember:
            self.states.pop(0)
        self.states.append(current_game_state)

    def save_action(self, current_action):
        state_table_length = len(self.states)
        current_state = self.states[state_table_length - 1]
        current_state.append(current_action)

    def dump_state(self):
        game_state_vector = list()
        if len(self.states) < GameState.frames_to_remember:
            # for first frames append with zeros
            missing_states = GameState.frames_to_remember - len(self.states)
            for x in range(0, missing_states * self.state_length):
                game_state_vector.append(0)

        for state in self.states:
            game_state_vector.extend(state)

        return game_state_vector

    def print_state(self):
        print(','.join(map(str, self.dump_state())))

    def update_game_state(self, mobs, player, bullets, frame_count):
        state = list()
        # state.extend(player.dump_state_vector())
        state.append(player.dump_state_vector()[1] % 6)

        # state["speedx"] = self.speedx
        # state["speedy"] = self.speedy
        # state["distance"] = round(sqrt((player_x - mob_x) * (player_x - mob_x)
        #                       + (player_y - mob_y) * (player_y - mob_y)))
        # state["dist_x"] = player_x - mob_x
        # state["dist_y"] = player_y - mob_y
        #
        # state['mob_x'] = mob_x
        # state['mob_y'] = mob_y

        # x, y
        mob_positions = [[0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0]]

        for mob in mobs.sprites():
            mob_state = mob.dump_state(player)
            pos_x = mob_state['mob_x'] % 6
            pos_y = mob_state['mob_y'] % 8
            mob_positions[pos_x][pos_y] = mob_positions[pos_x][pos_y] + 1

        for column in mob_positions:
            state.extend(column)

        self.__save_game_state(state)


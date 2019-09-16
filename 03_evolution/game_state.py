import numpy as np
import pygame
import random
from os import path
import time


class GameState:
    frames_to_remember = 4

    def __init__(self, player_vector_size, mob_vector_size, mob_size):
        self.states = list()
        self.player_vector_size = player_vector_size
        self.mob_vector_size = mob_vector_size
        self.mob_size = mob_size
        self.state_length = self.player_vector_size + self.mob_size * self.mob_vector_size + 1

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

    def update_game_state(self, mobs, player, bullets):
        state = list()
        state.extend(player.dump_state_vector())

        mob_vector_size = self.mob_vector_size
        for mob in mobs.sprites():
            mob_vec = mob.dump_state_vector(player)
            state.extend(mob_vec)

        # pad with empty mobs to have vector of the same size
        mob_length = len(mobs.sprites())
        for j in range((self.mob_size - mob_length) * mob_vector_size):
            state.append(0)

        self.__save_game_state(state)

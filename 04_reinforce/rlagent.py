from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers.core import Dense, Dropout
from keras.utils import to_categorical
import random
import numpy as np
import pandas as pd


class RLAgent:
    input_vector_size: object
    possible_moves = [0, 1, 2, 3, 4, 5]

    def __init__(self, input_vector_size):
        self.reward = 0
        self.gamma = 0.9
        self.dataframe = pd.DataFrame()
        self.short_memory = np.array([])
        self.agent_target = 1
        self.agent_predict = 0
        self.learning_rate = 0.0005
        self.epsilon = 0
        self.actual = []
        self.memory = []
        self.input_vector_size = input_vector_size
        self.model = self.network()
        #self.model = self.network("weights_150_5000_80.hdf5")

    def get_state(self, state):
        return np.asarray(state)

    def set_reward(self, score_increase, running):
        self.reward = 0
        if not running:
            self.reward = -10
            return self.reward
        if score_increase > 0:
            self.reward = 10 * score_increase
        return self.reward

    def network(self, weights=None):
        no_of_possible_moves = len(RLAgent.possible_moves)
        model = Sequential()
        model.add(Dense(output_dim=120, activation='relu', input_dim=self.input_vector_size))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=120, activation='relu'))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=120, activation='relu'))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=no_of_possible_moves, activation='softmax'))
        opt = Adam(self.learning_rate)
        model.compile(loss='mse', optimizer=opt)

        if weights:
            model.load_weights(weights)
        return model

    def remember(self, state, action, reward, next_state, running):
        self.memory.append((state, action, reward, next_state, not running))

    def replay_new(self, memory):
        if len(memory) > 5000:
            minibatch = random.sample(memory, 5000)
        else:
            minibatch = memory
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(np.array([next_state]))[0])
            target_f = self.model.predict(np.array([state]))
            target_f[0][np.argmax(action)] = target
            self.model.fit(np.array([state]), target_f, epochs=2, verbose=0)

    def train_short_memory(self, state, action, reward, next_state, running):
        target = reward
        if running:
            target = reward + self.gamma * np.amax(self.model.predict(next_state.reshape((1, self.input_vector_size)))[0])
        target_f = self.model.predict(state.reshape((1, self.input_vector_size)))
        target_f[0][np.argmax(action)] = target
        self.model.fit(state.reshape((1, self.input_vector_size)), target_f, epochs=2, verbose=0)

    @staticmethod
    def to_categorical(category):
        return to_categorical(category, num_classes=len(RLAgent.possible_moves))

    @staticmethod
    def from_categorical(categorical):
        if np.array_equal(categorical, [1, 0, 0, 0, 0, 0]):
            return 0
        if np.array_equal(categorical, [0, 1, 0, 0, 0, 0]):
            return 1
        if np.array_equal(categorical, [0, 0, 1, 0, 0, 0]):
            return 2
        if np.array_equal(categorical, [0, 0, 0, 1, 0, 0]):
            return 3
        if np.array_equal(categorical, [0, 0, 0, 0, 1, 0]):
            return 4
        if np.array_equal(categorical, [0, 0, 0, 0, 0, 1]):
            return 5
        return 0

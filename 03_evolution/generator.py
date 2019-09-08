import sys
import re
import os
import score_utils as sc
import random

generation = int(sys.argv[1])
path_to_evolution = "./evolution/"


def load_moves(file_name):
    with open(file_name, 'r') as seq_file:
        return seq_file.readlines()


def new_moves_generator(moves_to_extend, variant):
    variants_and_moves = {"1": 0, "2": 1, "3": 2, "4": 4, "5": 5}
    moves_to_extend.append("\n" + str(variants_and_moves[variant]))
    moves_to_extend.append("\n" + str(random.randint(0, 5)))
    moves_to_extend.append("\n" + str(variants_and_moves[variant]))
    moves_to_extend.append("\n" + str(random.randint(0, 5)))
    moves_to_extend.append("\n" + str(variants_and_moves[variant]))
    moves_to_extend.append("\n" + str(random.randint(0, 5)))
    moves_to_extend.append("\n" + str(variants_and_moves[variant]))
    moves_to_extend.append("\n" + str(random.randint(0, 5)))
    moves_to_extend.append("\n" + str(variants_and_moves[variant]))
    moves_to_extend.append("\n" + str(random.randint(0, 5)))
    return moves_to_extend


# candidate { "seq_file", "generation", "variant", "score", "time" }
# possible moves
# 0 - left, 1 - right, 2 - shoot, 3 - nothing,
# 4 - left + shoot, 5 - right + shoot
def evolve(candidate, generation):
    moves = load_moves(candidate["seq_file"])
    next_generation = list()
    variants_and_moves = {"1": 0, "2": 1, "3": 2, "4": 4, "5": 5}

    new_generation = int(generation) + 1
    for v in variants_and_moves.keys():
        new_candidate = dict()
        new_candidate["generation"] = new_generation
        new_candidate["variant"] = v
        new_candidate["moves"] = new_moves_generator(moves.copy(), v)
        next_generation.append(new_candidate)
    return next_generation


# new_moves = [ { "generation", "variant", "moves" }, .. ]
def save_new_moves(new_moves, path_to_evolution):
    for new_move in new_moves:
        filename = os.path.join(path_to_evolution, "gen_"
                                + str(new_move["generation"]) + "_"
                                + new_move["variant"] + ".seq")
        with open(filename, 'w') as out:
            out.writelines(new_move["moves"])
        print(filename + " generated")


generations_metada = dict()

if generation > 1:
    generations_metada = sc.parse_generation_metadata(generation - 1, path_to_evolution)

generations_metada.update(sc.parse_generation_metadata(generation, path_to_evolution))

candidate = sc.get_best_seqs(generations_metada, "score")
new_moves = evolve(candidate, generation)
save_new_moves(new_moves, path_to_evolution)

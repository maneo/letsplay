import sys
import re
import os
import score_utils as sc
import random

generation = int(sys.argv[2])
path_to_evolution = sc.path_to_evolution()


def load_moves(file_name):
    with open(file_name, 'r') as seq_file:
        raw_seq = seq_file.readlines()
        clean_seq = list()
        for move in raw_seq:
            clean_seq.append(move.rstrip())
        return clean_seq


# 0 - left, 1 - right, 2 - shoot, 3 - nothing,
# 4 - left + shoot, 5 - right + shoot

def new_moves_generator(moves_to_extend, variant):
    variants_and_moves = {"1": 0, "2": 1, "3": 2, "4": 4, "5": 5}
    moves_to_extend.append(str(variants_and_moves[variant]))
    return moves_to_extend


def new_moves_generator_kruk(moves_to_extend, variant):
    variants_and_moves = {"1": 0, "2": 1, "3": 2, "4": 4, "5": 5}
    moves_to_extend.append(str(variants_and_moves[variant]))
    moves_to_extend.append(str(random.randint(0, 5)))
    moves_to_extend.append(str(variants_and_moves[variant]))
    moves_to_extend.append(str(random.randint(0, 5)))
    moves_to_extend.append(str(variants_and_moves[variant]))
    moves_to_extend.append(str(random.randint(0, 5)))
    moves_to_extend.append(str(variants_and_moves[variant]))
    moves_to_extend.append(str(random.randint(0, 5)))
    moves_to_extend.append(str(variants_and_moves[variant]))
    moves_to_extend.append(str(random.randint(0, 5)))
    return moves_to_extend


def new_moves_generator_smok(moves_to_extend, variant):
    variants_and_moves = [
                           ["0", "4", "0", "4", "0", "4"],
                           ["1", "5", "1", "5", "1", "5"],
                           ["4", "4", "4", "4", "4", "4"],
                           ["5", "5", "5", "5", "5", "5"],
                           random_moves(6)
                         ]
    random_variant = random.randint(0, 4)
    moves_to_extend.extend(variants_and_moves[random_variant])
    return moves_to_extend


def random_moves(how_many):
    sequence = list()
    for i in range(0, how_many):
        random_move = str(random.randint(0, 5))
        sequence.append(random_move)
    return sequence


def crossover(parent1_moves, parent2_moves):
    offspring_moves = parent1_moves.copy()
    noise = random.randint(0, 1)

    for i in range(0, len(parent2_moves)):
        if noise == 1 and i % 2 == 0:
            offspring_moves[i] = parent2_moves[i]

        if noise == 0 and i % 2 == 1:
            offspring_moves[i] = parent2_moves[i]

    return offspring_moves


def mutate(offspring_moves, how_many_mutations):
    mutant_moves = offspring_moves.copy()

    for i in range(0, how_many_mutations):
        mutation_idx = random.randint(0, len(offspring_moves) - 1)
        mutant_moves[mutation_idx] = str(random.randint(0, 5))

    return mutant_moves


# candidate { "seq_file", "generation", "variant", "score", "time" }
# possible moves
# 0 - left, 1 - right, 2 - shoot, 3 - nothing,
# 4 - left + shoot, 5 - right + shoot
def evolve(candidates, generation):
    candidate = candidates[0]
    moves = load_moves(candidate["seq_file"])
    next_generation = list()
    variants_and_moves = {"1": 0, "2": 1, "3": 2, "4": 4, "5": 5}

    new_generation = int(generation) + 1
    for v in variants_and_moves.keys():
        new_candidate = dict()
        new_candidate["generation"] = new_generation
        new_candidate["variant"] = v
        new_candidate["moves"] = new_moves_generator(moves.copy(), v)
        # new_candidate["moves"] = new_moves_generator_kruk(moves.copy(), v)
        # new_candidate["moves"] = new_moves_generator_smok(moves.copy(), v)
        next_generation.append(new_candidate)

    for i in range(0, 4):
        moves_to_mutate = next_generation[i]["moves"]
        how_many_mutation = round(len(moves_to_mutate) / 10)
        next_generation[i]["moves"] = mutate(moves_to_mutate, how_many_mutation)

    return next_generation


def evolve_fixed_length(candidates, generation):
    best_parent1 = candidates[0]
    best_parent1_moves = load_moves(best_parent1["seq_file"])

    best_parent2 = candidates[1]
    best_parent2_moves = load_moves(best_parent2["seq_file"])

    best_parent3 = candidates[2]
    best_parent3_moves = load_moves(best_parent3["seq_file"])

    offspring_1_2_moves = crossover(best_parent1_moves, best_parent2_moves)
    offspring_3_1_moves = crossover(best_parent3_moves, best_parent1_moves)
    offspring_2_3_moves = crossover(best_parent2_moves, best_parent3_moves)
    mutant_1_2_moves = mutate(offspring_1_2_moves, random.randint(100, 200))
    mutant_3_1_moves = mutate(offspring_3_1_moves, random.randint(100, 200))

    new_generation = int(generation) + 1
    new_candidates = list()

    new_candidates.append(get_offspring(offspring_1_2_moves, 1, new_generation))
    new_candidates.append(get_offspring(offspring_3_1_moves, 2, new_generation))
    new_candidates.append(get_offspring(offspring_2_3_moves, 3, new_generation))
    new_candidates.append(get_offspring(mutant_1_2_moves, 4, new_generation))
    new_candidates.append(get_offspring(mutant_3_1_moves, 5, new_generation))

    return new_candidates


def get_offspring(moves, variant, generation):
    new_candidate = dict()
    new_candidate["generation"] = generation
    new_candidate["variant"] = variant
    new_candidate["moves"] = moves
    return new_candidate


# new_moves = [ { "generation", "variant", "moves" }, .. ]
def save_new_moves(new_moves, path_to_evolution):
    for new_move in new_moves:
        filename = os.path.join(path_to_evolution, "gen_"
                                + str(new_move["generation"]) + "_"
                                + str(new_move["variant"]) + ".seq")
        with open(filename, 'w') as out:
            for move in new_move["moves"]:
                out.write(str(move) + "\n")
        print(filename + " generated")


generations_metada = dict()

if generation > 1:
    generations_metada = sc.parse_generation_metadata(generation - 1, path_to_evolution)

generations_metada.update(sc.parse_generation_metadata(generation, path_to_evolution))

candidates = sc.get_best_candidates(generations_metada)

# todo test both games scenario
# new_moves = evolve(candidates, generation)
new_moves = evolve_fixed_length(candidates, generation)
save_new_moves(new_moves, path_to_evolution)

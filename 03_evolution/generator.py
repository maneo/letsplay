import sys
import re
import os

generation = int(sys.argv[1])
path_to_evolution = "./evolution/"


def parse_score(file_name):
    regexp = "gen\_(\d+)\_(\d+)\_dead_s_(\d+)_t_(\d+)\.seq"
    metadata_match = re.search(regexp, file_name, re.IGNORECASE)

    if metadata_match:
        return metadata_match.group(1), metadata_match.group(2), \
               metadata_match.group(3), metadata_match.group(4)

    return 0, 0, 0, 0


def parse_generation_metadata(generation, path_to_evolution):
    files = []
    generation_data = dict()
    for r, d, f in os.walk(path_to_evolution):
        for file in f:
            if ('gen_' + str(generation) in file) \
                    and ('_dead_s' in file) \
                    and ('.log' not in file):
                files.append(os.path.join(r, file))
                data = dict()
                data['seq_file'] = os.path.join(r, file)
                data['generation'], data['variant'], data['score'], data['time'],  = parse_score(file)
                generation_data[file] = data

    return generation_data


def get_best_seqs(generations_metadata, best_by_field):
    best_score = 0
    best_key = ""
    for key in generations_metadata:
        score = int(generations_metada[key][best_by_field])
        if score > best_score:
            best_score = score
            best_key = key
    return generations_metada[best_key]


def load_moves(file_name):
    with open(file_name, 'r') as seq_file:
        return seq_file.readlines()


# candidate { "seq_file", "generation", "variant", "score", "time" }
# possible moves
# 0 - left, 1 - right, 2 - shoot, 3 - nothing,
# 4 - left + shoot, 5 - right + shoot
def evolve(candidate):
    moves = load_moves(candidate["seq_file"])
    next_generation = list()
    variants_and_moves = {"1": 0, "2": 1, "3": 2, "4": 4, "5": 5}

    new_generation = int(candidate["generation"]) + 1
    for v in variants_and_moves.keys():
        new_candidate = dict()
        new_candidate["generation"] = new_generation
        new_candidate["variant"] = v

        new_moves = moves.copy()
        new_moves.append(str(variants_and_moves[v]) + "\n")
        new_candidate["moves"] = new_moves
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
        print(filename + "generated")


generations_metada = dict()

if generation > 1:
    generations_metada = parse_generation_metadata(generation - 1, path_to_evolution)

generations_metada.update(parse_generation_metadata(generation, path_to_evolution))

candidate = get_best_seqs(generations_metada, "score")
new_moves = evolve(candidate)
save_new_moves(new_moves, path_to_evolution)

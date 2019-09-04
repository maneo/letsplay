import random
from os import path
import sys
import re
import os

generation = int(sys.argv[1])
path = "./evolution/"

# for sekwencja_ruchów w najmocniejsze_sekwencje:
#     proponowana_sekwencja_ruchów = generuj_kolejny_ruch(numer_pokolenia, sekwencja)
#     rzeczywista_sekwencja_ruchów, score = graj(proponowana_sekwencja_ruchów, numer_pokolenia)
#     // (jezeli sekwencja skonczy się przed śmiercią - dopełniaj ją jednym ruchem - strzałem)
#     zapisz_sekwencje_wynikową
#     zapisz
#     dane
#     treningowe


# wczytaj sekwencje ruchow

def parse_score(file_name):
    regexp = "gen\_(\d+)\_(\d+)\_dead_s_(\d+)_t_(\d+)\.seq"
    metadata_match = re.search(regexp, file_name, re.IGNORECASE)

    if metadata_match:
        return metadata_match.group(1), metadata_match.group(2), \
               metadata_match.group(3), metadata_match.group(4)

    return 0, 0, 0, 0


def parse_generation_metadata(generation):
    files = []
    generation_data = dict()
    for r, d, f in os.walk(path):
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


def get_best_seqs_by_score(generations_metadata):
    best_score = 0
    best_key = ""
    for key in generations_metadata:
        score = int(generations_metada[key]['score'])
        if score > best_score:
            best_score = score
            best_key = key
    return best_key, generations_metada[best_key]


def load_moves(file_name):
    with open(file_name, 'r') as seq_file:
        return seq_file.readlines()


def evolve(candidate, key_name):
    moves = load_moves(candidate)
    # load moves seq for best candidates
    # generate new moves
    # update generation and variant

    return candidate


def save_new_moves(new_moves):
    # zapisz nową sekwencje ruchów

    pass


generations_metada = dict()

if generation > 1:
    generations_metada = parse_generation_metadata(generation - 1)

generations_metada.update(parse_generation_metadata(generation))

seq_file, candidate = get_best_seqs_by_score(generations_metada)
new_moves = evolve(candidate)
save_new_moves(new_moves)

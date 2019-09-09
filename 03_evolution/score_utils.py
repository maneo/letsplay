import re
import os
import sys


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
                data['dead_seq_file'] = os.path.join(r, file)
                data['generation'], data['variant'], data['score'], data['time'],  = parse_score(file)
                seq_file_name = "gen_" + data['generation'] + "_" + data['variant'] + ".seq"
                data['seq_file'] = os.path.join(r, seq_file_name)
                generation_data[file] = data

    return generation_data


def get_best_seqs(generations_metadata, best_by_field):
    best_score = 0
    best_key = ""
    for key in generations_metadata:
        score = int(generations_metadata[key][best_by_field])
        if score > best_score:
            best_score = score
            best_key = key
    return generations_metadata[best_key]


def path_to_evolution():
    experiment_name = sys.argv[1]
    return "./evolution/" + experiment_name + "/"


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
    generation_data = {"1": list(), "2": list(), "3": list(), "4": list(), "5": list()}
    for r, d, f in os.walk(path_to_evolution):
        for file in f:
            if ('gen_' + str(generation) in file) \
                    and ('_dead_s' in file) \
                    and ('.log' not in file):
                files.append(os.path.join(r, file))
                data = dict()
                data['dead_seq_file'] = os.path.join(r, file)
                data['generation'], data['variant'], data['score'], data['time'],  = parse_score(file)
                seq_file_name = "gen_" + str(data['generation']) + "_" + str(data['variant']) + ".seq"
                data['seq_file'] = os.path.join(r, seq_file_name)
                generation_data[data['variant']].append(data)

    return generation_data


def calc_avg(variant_evaluations, best_by_field):
    summary = 0
    for evaluation in variant_evaluations:
        summary = summary + int(evaluation[best_by_field])
    return round(summary / len(variant_evaluations))


def get_best_candidates(generations_metadata):
    dict_by_score = dict()
    for variant in generations_metadata:
        variant_evaluations = generations_metadata[variant]
        avg_score = calc_avg(variant_evaluations, "score")
        avg_time = calc_avg(variant_evaluations, "time")

        new_representation = dict()
        new_representation["generation"] = variant_evaluations[0]["generation"]
        new_representation["variant"] = variant_evaluations[0]["variant"]
        new_representation["seq_file"] = variant_evaluations[0]["seq_file"]
        new_representation["score"] = avg_score
        new_representation["time"] = avg_time

        dict_by_score[avg_score] = new_representation

    sorted_candidates = list()
    for key in sorted(dict_by_score.keys(), reverse=True):
        sorted_candidates.append(dict_by_score[key])

    return sorted_candidates


def path_to_evolution():
    experiment_name = sys.argv[1]
    return "./evolution/" + experiment_name + "/"


import sys
import score_utils as sc

generation = int(sys.argv[1])
path_to_evolution = "./evolution/"

generations_metada = dict()

if generation > 1:
    generations_metada = sc.parse_generation_metadata(generation - 1, path_to_evolution)

generations_metada.update(sc.parse_generation_metadata(generation, path_to_evolution))

candidate = sc.get_best_seqs(generations_metada, "score")

print(candidate['score'])

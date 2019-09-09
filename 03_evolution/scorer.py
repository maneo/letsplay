import sys
import score_utils as sc

generation = int(sys.argv[2])
path_to_evolution = sc.path_to_evolution()

generations_metadata = dict()

if generation > 1:
    generations_metadata = sc.parse_generation_metadata(generation - 1, path_to_evolution)

generations_metadata.update(sc.parse_generation_metadata(generation, path_to_evolution))

candidate = sc.get_best_seqs(generations_metadata, "score")

print(candidate['score'])

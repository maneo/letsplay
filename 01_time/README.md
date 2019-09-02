
how to run evaluation?

* activate conda env
* run bash -x evaluate.sh

files agenda:
* eval_*e.log - results of particular model evaluation
* *.pkl - trained models
* mlp_*pkl - multi layered perceptron models
* xgb_*pkl - xgboost models
* tail*.log - training data for models

only time:
* step 1: one game -- too few observations - to perform generalization, plays poorly
* step 2: is neural network able to generalize that? maybe with more data? - yes, but..

drawbacks?
* when last too long (longer than longest game) model will lost his ability to decide

only time % 126 and action
* minimal data set showing basic strategy looped

drawbacks?
* does not take into account position of rocks, cannot escape from side attack

comaprision

evaluation only_time (forest) with 10 attempts, resulted with, avg time: 77.1 and avg score: 109.3
evaluation synth_126 (forest) with 10 attempts, resulted with, avg time: 154.2 and avg score: 237.7

evaluation only_time (mlp) with 10 attempts, resulted with, avg time: 83.3 and avg score: 122
evaluation synth_126 (mlp) with 10 attempts, resulted with, avg time: 193.7 and avg score: 296

evaluation only_time (xgb) with 10 attempts, resulted with, avg time: 37.5 and avg score: 92.8
evaluation synth_126 (xgb) with 10 attempts, resulted with, avg time: 94.9 and avg score: 250.3
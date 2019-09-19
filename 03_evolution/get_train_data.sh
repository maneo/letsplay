#!/usr/bin/env bash

#rm train.csv

function get_data() {
    python shmup-play.py best_moves ${variant} > training-data-${variant}.log
    tail -n +3 training-data-${variant}.log >> train-data-${variant}.csv
    sed -i '' -e '$ d' train-data-${variant}.csv
    was_alive=`tail -n 1 training-data-${variant}.log | grep True`
    if [[ -z "${was_alive}" ]]
    then
        # rm train-data-${variant}.csv
        rm training-data-${variant}.log
    fi
}

variant="1_5"
get_data

variant="1_3"
get_data

variant="1_9"
get_data

variant="30_3"
get_data

variant="31_6"
get_data

variant="21_4"
get_data

variant="40_4"
get_data

variant="10_1"
get_data

variant="10_4"
get_data

variant="20_5"
get_data

variant="21_3"
get_data

variant="3_1"
get_data

variant="1_8"
get_data

variant="6_1"
get_data

variant="40_2"
get_data

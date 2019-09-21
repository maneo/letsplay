#!/usr/bin/env bash

function get_data() {
    python shmup-play.py best_moves ${variant} > training-data-${variant}.log
    tail -n +3 training-data-${variant}.log > train-data-tmp-${variant}.csv
    sed -i '' -e '$ d' train-data-tmp-${variant}.csv
    was_alive=`tail -n 1 training-data-${variant}.log | grep True`
    if [[ ! -z "${was_alive}" ]]
    then
        cat train-data-tmp-${variant}.csv >> train-data-${variant}.csv
    fi
    rm train-data-tmp-${variant}.csv
    rm training-data-${variant}.log

}

variant="1_5"
get_data &

variant="1_3"
get_data &

variant="1_4"
get_data &

variant="1_6"
get_data &

variant="1_7"
get_data &

variant="1_8"
get_data &

variant="1_9"
get_data &

variant="2_4"
get_data &

wait

variant="3_1"
get_data &

variant="5_5"
get_data &

variant="6_1"
get_data &

variant="10_1"
get_data &

variant="10_4"
get_data &

variant="13_1"
get_data &

variant="13_5"
get_data &

variant="15_4"
get_data &

wait

variant="17_3"
get_data &

variant="18_2"
get_data &

variant="19_2"
get_data &

variant="20_5"
get_data &

variant="21_3"
get_data &

variant="21_4"
get_data &

variant="30_3"
get_data &

variant="31_6"
get_data &

wait

variant="33_5"
get_data &

variant="34_4"
get_data &

variant="40_2"
get_data &

variant="40_4"
get_data &

variant="10_2"
get_data &

variant="21_2"
get_data &

wait

rm ./evolution/best_moves/gen*dead*.seq
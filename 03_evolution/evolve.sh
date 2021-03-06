#!/usr/bin/env bash

generation=1
max_score=0
gradient=0

iteration_without_improvement=0
recent_gain_generation=0
experiment_name=$1

base_dir_name="./evolution/${experiment_name}"
logs_dir="${base_dir_name}/logs"

mkdir -p ${logs_dir}

function run_variant_parallel() {

  # run the same move seq x4 to have less accidental score
  logfile="${logs_dir}/dead_gen_${variant}_run_1.log"
  python shmup-play.py "${experiment_name}" "${variant}" >> ${logfile} &

  logfile="${logs_dir}/dead_gen_${variant}_run_2.log"
  python shmup-play.py "${experiment_name}" "${variant}" >> ${logfile} &

  logfile="${logs_dir}/dead_gen_${variant}_run_3.log"
  python shmup-play.py "${experiment_name}" "${variant}" >> ${logfile} &

  logfile="${logs_dir}/dead_gen_${variant}_run_4.log"
  python shmup-play.py "${experiment_name}" "${variant}" >> ${logfile} &

}

while [[ ${iteration_without_improvement} -le 1 ]] || [[ ${generation} -le 1 ]]
do
  variant="${generation}_1"
  run_variant_parallel

  variant="${generation}_2"
  run_variant_parallel

  variant="${generation}_3"
  run_variant_parallel

  variant="${generation}_4"
  run_variant_parallel

  variant="${generation}_5"
  run_variant_parallel

  variant="${generation}_6"
  run_variant_parallel

  wait

  python generator.py "${experiment_name}" "${generation}"

  current_score=`python scorer.py "${experiment_name}" "${generation}"`
  gradient=`expr ${current_score} - ${max_score}`

  echo "current_score: ${current_score} - max_score: ${max_score} - generation: ${generation} - gradient: ${gradient}"

  max_score=$(( max_score > current_score ? max_score : current_score ))

  echo "${generation},${max_score},${current_score}" >> "${base_dir_name}/progress.log"

  if [[ ${gradient} -lt 0 ]]
  then
    ((iteration_without_improvement++))
  else
    iteration_without_improvement=0
    recent_gain_generation=${generation}
  fi

  echo "iterations without improvement: ${iteration_without_improvement}"

  ((generation++))
done
#!/usr/bin/env bash

generation=1
prev_score=0
gradient=0
experiment_name=$1

base_dir_name="./evolution/${experiment_name}"
logs_dir="${base_dir_name}/logs"

while [[ ${gradient} -gt 0 ]] || [[ ${generation} -le 100 ]]
do
  variant="${generation}_1"
  logfile="${logs_dir}/dead_gen_${variant}.log"
  python shmup-play.py "${experiment_name}" "${variant}" >> ${logfile} &

  variant="${generation}_2"
  logfile="${logs_dir}/dead_gen_${variant}.log"
  python shmup-play.py "${experiment_name}" "${variant}" >> ${logfile} &

  variant="${generation}_3"
  logfile="${logs_dir}/dead_gen_${variant}.log"
  python shmup-play.py "${experiment_name}" "${variant}" >> ${logfile} &

  variant="${generation}_4"
  logfile="${logs_dir}/dead_gen_${variant}.log"
  python shmup-play.py "${experiment_name}" "${variant}" >> ${logfile} &

  variant="${generation}_5"
  logfile="${logs_dir}/dead_gen_${variant}.log"
  python shmup-play.py "${experiment_name}" "${variant}" >> ${logfile} &

  wait
  python generator.py "${experiment_name}" "${generation}"

  current_score=`python scorer.py "${experiment_name}" "${generation}"`
  gradient=`expr ${current_score} - ${prev_score}`
  echo "current_score: ${current_score} - prev_score: ${prev_score} - generation: ${generation} - gradient: ${gradient}"
  prev_score=$(( prev_score > current_score ? prev_score : current_score ))

  echo "${generation},${prev_score},${current_score}" >> "${base_dir_name}/progress.log"

  ((generation++))
done
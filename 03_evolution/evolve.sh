#!/usr/bin/env bash

generation=1
prev_score=0
gradient=0

while [[ ${gradient} -gt 0 ]] || [[ ${generation} -le 1000 ]]
do
  variant="${generation}_1"
  logfile="./evolution/logs/dead_gen_${variant}.log"
  python shmup-play.py "${variant}" >> ${logfile}

  variant="${generation}_2"
  logfile="./evolution/logs/dead_gen_${variant}.log"
  python shmup-play.py "${variant}" >> ${logfile}

  variant="${generation}_3"
  logfile="./evolution/logs/dead_gen_${variant}.log"
  python shmup-play.py "${variant}" >> ${logfile}

  variant="${generation}_4"
  logfile="./evolution/logs/dead_gen_${variant}.log"
  python shmup-play.py "${variant}" >> ${logfile}

  variant="${generation}_5"
  logfile="./evolution/logs/dead_gen_${variant}.log"
  python shmup-play.py "${variant}" >> ${logfile}

  python generator.py "${generation}"

  current_score=`python scorer.py "${generation}"`
  gradient=`expr ${current_score} - ${prev_score}`
  echo "current_score: ${current_score} - prev_score: ${prev_score} - generation: ${generation}"
  prev_score=${current_score}

  ((generation++))
done
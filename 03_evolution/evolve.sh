#!/usr/bin/env bash

generation=1

while [[ ${generation} -le 3 ]]
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
  ((generation++))
done
#!/usr/bin/env bash


function eval_experiment() {

	logfile="eval_${model_name}.log"
	echo "evaluation of ${model_name}"

	while [ $i -le $max_attempts ]
	do
	 python shmup-play-ai.py ${model_name} >> $logfile
	 ((i++))
	done

	# print("time: {} sec, score: {}".format(round(end - game_start_time), score))
	avgtime=`cat $logfile | grep time | cut -d "," -f 1 | cut -d ":" -f 2 | cut -d " " -f 2 | awk '{ total += $1; count++ } END { print total/count }'`
	avgscore=`cat $logfile | grep time | cut -d "," -f 2 | cut -d ":" -f 2 | cut -d " " -f 2 | awk '{ total += $1; count++ } END { print total/count }'`

	echo "evaluation ${model_name} with $i attempts, resulted with, avg time: ${avgtime} and avg score: ${avgscore}"

}

#model_name="logit"
#max_attempts=9
#i=0
#
#eval_experiment
#
#
#model_name="xgb"
#max_attempts=9
#i=0
#
#eval_experiment


model_name="mlp"
max_attempts=9
i=0

eval_experiment

#
#model_name="forest"
#max_attempts=9
#i=0
#
#eval_experiment
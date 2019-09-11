#!/usr/bin/env bash


function eval_experiment() {

	logfile="eval_${experiment_name}.log"
	echo "evaluation of ${experiment_name}"

	rm $logfile

	while [[ $i -le ${max_attempts} ]]
	do
	 python shmup-play-${experiment_name}.py >> $logfile
	 ((i++))
	done

	# print("time: {} sec, score: {}".format(round(end - game_start_time), score))
	avgtime=`cat $logfile | grep time | cut -d "," -f 1 | cut -d ":" -f 2 | cut -d " " -f 2 | awk '{ total += $1; count++ } END { print total/count }'`
	avgscore=`cat $logfile | grep time | cut -d "," -f 2 | cut -d ":" -f 2 | cut -d " " -f 2 | awk '{ total += $1; count++ } END { print total/count }'`

	echo "evaluation ${experiment_name} with $i attempts, resulted with, avg time: ${avgtime} and avg score: ${avgscore}"

}

experiment_name="only_time"
max_attempts=9
i=0

eval_experiment

experiment_name="synth_126"
i=0

eval_experiment

experiment_name="random"
i=0

experiment_name="killemall"
i=0

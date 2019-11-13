#!/usr/bin/env bash

population=1

base_dir_name="./evolution"
logs_dir="${base_dir_name}/logs"

while [[ ${population} -le 2 ]]
do
    experiment_name="${population}_experiment_base"
    cp -R "${base_dir_name}/template" "${base_dir_name}/${experiment_name}"
#	cp -R "${base_dir_name}/template_fixed_game" "${base_dir_name}/${experiment_name}"
	date
	bash evolve.sh "${experiment_name}" > "${base_dir_name}/${experiment_name}/experiment.log"
	date
	((population++))
done
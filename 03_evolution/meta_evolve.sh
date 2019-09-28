#!/usr/bin/env bash

population=1

base_dir_name="./evolution"
logs_dir="${base_dir_name}/logs"

while [[ ${population} -le 50 ]]
do
#	cp -R "${base_dir_name}/template_fixed_game" "${base_dir_name}/${population}_experiment"
	cp -R "${base_dir_name}/template" "${base_dir_name}/${population}_experiment"
	date
	bash evolve.sh "${population}_experiment" > "${base_dir_name}/${population}_experiment/experiment.log"
	date
	((population++))
done
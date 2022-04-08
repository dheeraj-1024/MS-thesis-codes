#!/bin/bash

list="210K 220K 230K 240K 250K 260K 273K 285K 300K"
source /home/dheeraj/folder_de_source_files/albert
printf "LOADING COMPLETE\n"
printf "210\n14454\n" | python /home/dheeraj/project/param_traj/210K/analysis_2.0/test.py
printf "210K done"
printf "220\n8913\n" | python /home/dheeraj/project/param_traj/220K/analysis_2.0/test.py
printf "220K done"
printf "230\n4466\n" | python /home/dheeraj/project/param_traj/230K/analysis_2.0/test.py
printf "230K done"
printf "240\n1258\n" | python /home/dheeraj/project/param_traj/240K/analysis_2.0/test.py
printf "240K done"
printf "250\n223\n" | python /home/dheeraj/project/param_traj/250K/analysis_2.0/test.py
printf "250K done"
printf "260\n44\n" | python /home/dheeraj/project/param_traj/260K/analysis_2.0/test.py
printf "260K done"
printf "273\n26\n" | python /home/dheeraj/project/param_traj/273K/analysis_2.0/test.py
printf "FULL TASK COMPLETE \n EXITING SCRIPT \n"

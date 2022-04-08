#!/bin/bash

list="210K 220K 230K 240K 250K 260K 273K 285K 300K"
for i in $list
do 
	cp /home/dheeraj/project/param_traj/200K/analysis/Lambda_calculator.py /home/dheeraj/project/param_traj/$i/analysis
done
source /home/dheeraj/folder_de_source_files/albert
printf "LOADING COMPLETE\n"
printf "/home/dheeraj/project/param_traj/210K/prod.tpr\n/home/dheeraj/project/param_traj/210K/md.xtc\n14454\n" | python /home/dheeraj/project/param_traj/210K/analysis/Lambda_calculator.py
printf "210K done"
printf "/home/dheeraj/project/param_traj/220K/prod.tpr\n/home/dheeraj/project/param_traj/220K/md.xtc\n8913\n" | python /home/dheeraj/project/param_traj/220K/analysis/Lambda_calculator.py
printf "220K done"
printf "/home/dheeraj/project/param_traj/230K/prod.tpr\n/home/dheeraj/project/param_traj/230K/md.xtc\n4466\n" | python /home/dheeraj/project/param_traj/230K/analysis/Lambda_calculator.py
printf "230K done"
printf "/home/dheeraj/project/param_traj/240K/prod.tpr\n/home/dheeraj/project/param_traj/240K/md.xtc\n1258\n" | python /home/dheeraj/project/param_traj/240K/analysis/Lambda_calculator.py
printf "240K done"
printf "/home/dheeraj/project/param_traj/250K/prod.tpr\n/home/dheeraj/project/param_traj/250K/md.xtc\n223\n" | python /home/dheeraj/project/param_traj/250K/analysis/Lambda_calculator.py
printf "250K done"
printf "/home/dheeraj/project/param_traj/260K/prod.tpr\n/home/dheeraj/project/param_traj/260K/md.xtc\n44\n" | python /home/dheeraj/project/param_traj/260K/analysis/Lambda_calculator.py
printf "260K done"
printf "/home/dheeraj/project/param_traj/273K/prod.tpr\n/home/dheeraj/project/param_traj/273K/md.xtc\n26\n" | python /home/dheeraj/project/param_traj/273K/analysis/Lambda_calculator.py
printf "FULL TASK COMPLETE \n EXITING SCRIPT \n"

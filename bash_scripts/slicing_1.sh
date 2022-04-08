#!/bin/bash

list="210K 220K 230K 240K 250K 260K 273K"
source /home/dheeraj/folder_de_source_files/albert
printf "LOADING COMPLETE\n"
for i in $list
do 
	cd /home/dheeraj/project/param_traj/$i/
	gmx_d trjconv -f md.xtc -o sliced_md_$i.xtc -fr modified_frame_$i.ndx
	printf "$i completed"
done

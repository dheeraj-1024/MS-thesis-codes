#!/bin/bash
source ~/folder_de_source_files/sara_ent
source ~/folder_de_source_files/file_de_source_1
printf "2\n" | trjordern -f md.xtc -s prod.gro -n index.ndx -com -point -da 1 -na 5 -vec 1.5665 1.5665 1.5665
source ~/folder_de_source_files/file_de_source_3
printf "3\n2\n" | g_permutemn -f ordered.xtc -s prod.gro -n index.ndx -m 5 -pbc -com
printf "3\n" | g_transent -f permute.xtc -s prod.gro -n index.ndx -pbc -norot -mwa -temperature 210

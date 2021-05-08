#!/bin/bash
#SBATCH --node=1
#SBATCH --time=24:00:00
#SBATCH --mem=120Gb
#SBATCH --job-name=lee.ting
#SBATCH --output=lee.ting.log
#SBATCH --partition=short
#SBATCH --cpus-perptask=4
#SBATCH --ntansks=1
source activate rmg_env
python $RMGPY/rmg.py input.py

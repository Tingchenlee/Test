#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=24:00:00
#SBATCH --mem=120Gb
#SBATCH --job-name=Rebrov_673
#SBATCH --output=lee.ting.log
#SBATCH --partition=short
#SBATCH --cpus-per-task=4
#SBATCH --ntasks=1
#SBATCH --mail-user=lee.ting@northeastern.edu
#SBATCH --mail-type=FAIL,END

source activate rmg_env
python $RMGPY/rmg.py input.py

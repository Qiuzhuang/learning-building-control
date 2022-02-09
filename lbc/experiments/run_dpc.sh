#!/bin/bash --login
#SBATCH --account=aumc
#SBATCH --job-name=dpc
#SBATCH --qos=high
#SBATCH --tasks-per-node=1
#SBATCH --nodes=1

set -x

source env.sh

python run_dpc.py --bsz $BATCH_SIZE --dr $DR_PROGRAM --dry-run $DRY_RUN \
    --num-epochs 2000 --results-dir $RESDIR


#!/bin/bash -l
#SBATCH --account=lp_h_ds_2023_2024
#SBATCH --cluster=wice
#SBATCH --nodes=1
#SBATCH --time=20:10:00

module load Python/3.11.3-GCCcore-12.3.0 

python -m venv myenvtest
source myenvtest/bin/activate

python -m pip install --upgrade pip
python -m pip install --upgrade pip setuptools

python -m pip install mmh3
python -m pip install pandas
python -m pip install scipy
python -m pip install numpy
python -m pip install faker


python main.py --m 2000000 --k 25 --data_type words

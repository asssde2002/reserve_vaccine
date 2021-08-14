#!/bin/bash

my_dir="${PWD}/reserve_vaccine"
echo "Start Crontab" >> ${my_dir}/execution.log
source $my_dir/venv/bin/activate
python3 $my_dir/src/main.py
deactivate
echo -e "Finish Crontab \n" >> ${my_dir}/execution.log

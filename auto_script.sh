#!/bin/bash

cd reserve_vaccine >& /dev/null
my_dir="${PWD}"
echo -e "$(date) \nStart Crontab" >> ${my_dir}/execution.log
source $my_dir/venv/bin/activate
python3 $my_dir/src/main.py
deactivate
echo -e "Finish Crontab \n" >> ${my_dir}/execution.log

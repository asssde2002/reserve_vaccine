#!/bin/bash

cd reserve_vaccine >& /dev/null
#my_dir="${PWD}"
echo -e "$(date) \nStart Crontab" >> execution.log
source venv/bin/activate
python3 src/main.py
deactivate
echo -e "Finish Crontab \n" >> execution.log

# Reserve Vaccine

## Setup
* Install package before executing
```
pip3 install -r requirements.txt
```
## Crontab
Make sure to set the time to reserve automatically
* Edit crontab
> crontab -e
* List crontab
> crontab -l
* Remove crontab
> crontab -r

* 欄位說明
 
> 1分鐘（0-59)

> 2小時（2-24）

> 3日期（1-31）

> 4月份（1-12；或英文縮寫Jan、Feb等）

> 5周幾（0-6，0為周日；或單詞縮寫Sun、Mon等）

> 6使用者名（執行命令時以此使用者的身份）

> 7要執行的命令（路徑)

* My setting of crontab
```
 30 8 * * 1-5 /bin/bash /Users/kingarthur/reserve_vaccine/auto_script.sh
```


## Personal Sensitive Data
* Copy "development.cfg" file and change its name to "production.cfg"

* The data in the file needs to be replaced with your personal data

## Virtual Environment

```
cd reserve_vaccine
source venv/bin/activate
```
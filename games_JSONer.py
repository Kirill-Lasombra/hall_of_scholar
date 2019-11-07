import json
import requests
import time
import os, sys

dd = int(input('Укажите день: '))
mm = int(input('Укажите месяц: '))
print("Формирую файл со всеми играми вышедшими {:02}.{:02}".format(dd,mm))

for yy in range(1988,2020):
    urls= 'https://api.games.mail.ru/pc/calendar/?date={:04}-{:02}-{:02}&page=1&filter=popular&limit=100'.format(yy,mm,dd)
    response = requests.get(urls)
    today = json.loads(response.text)
    fl = '{:02}.{:02}.txt'.format(dd,mm)
    if today['count'] != 0:

        with open(fl, "a") as td_fl:
            print("Игры {:04} года: \n".format(yy), file=td_fl)

        for aa in today['results']:
            with open(fl, "a") as td_fl:
                print(aa['name'], file=td_fl)
                print(aa['descr'], file=td_fl)
                print('\n', file=td_fl)
        with open(fl, "a") as td_fl:
            print('\n', file=td_fl)

    print ("The {:04} year is ready!".format(yy))

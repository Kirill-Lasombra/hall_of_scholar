import json
import requests
import time

dd = int(input('Укажите день: '))
mm = int(input('Укажите месяц: '))
print("Формирую файл со всеми играми вышедшими " + str('{:02}'.format(dd)) + '.' + str('{:02}'.format(mm)))
yy=1980

for yy in range(1988,2020):
    urls= 'https://api.games.mail.ru/pc/calendar/?date=' + str(yy) + '-' + str('{:02}'.format(mm)) + '-' + str('{:02}'.format(dd))+'&page=1&filter=popular&limit=30'
    response = requests.get(urls)
    today = json.loads(response.text)
    file= str('{:02}'.format(dd))+ '.' + str('{:02}'.format(mm)) + '.txt'
    fl = str('{:02}'.format(dd)) + '.' + str('{:02}'.format(mm)) + '.txt'
    with open(fl, "a") as td_fl:
        print("\n\nИгры " + str(yy) + " года: \n", file=td_fl)

    yy+=1
    rangelist = range(today['count'])
    aa = 0
    for aa in rangelist:
        name = today['results'][aa]['name'],
        descr = today['results'][aa]['descr'],
        game = name + descr
        aa += 1

        with open(fl, "a") as td_fl:
            print(game, file=td_fl)
    time.sleep (1)
    print ("The " + str(yy) + " is ready")

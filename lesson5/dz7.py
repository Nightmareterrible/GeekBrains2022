# По согласованию с преподавателем выполняю изменённое ДЗ : отпарсить курсы валют, полученные с сайта в формате JSON
import json
import requests

# получение динамики курса белорусского рубля по отношению к 100 Российским рублям за перид с 01.01.2021 по 05.05.2021
# необходимо использовать именно метод GET. Метод POST (как из dz2) не поддерживается сервером НацБанка РБ
r = requests.get("https://www.nbrb.by/api/exrates/rates/dynamics/298?startdate=2021-1-1&enddate=2021-5-5")
# тест соединения - записываем в файл
with open("dz7_out.txt", "w", encoding="utf-8") as w:
    w.write(r.text)
data = json.loads(r.text)

# выведем на какую дату курс повышался (значение было больше предыдущего) и понижался (значение меньше предыдущего
# а также запишем эти изменения в словарь {'up':[{date:cource}], 'down':[{date:course}]}
# использовал полученные на 3-ем занятии знания, чтобы не делать if dict[] is None, чтобы добавлять список
dynamics = {'up': [], 'down': []}
prev = data[0]['Cur_OfficialRate']
for i in data[1:]:
    if i['Cur_OfficialRate'] > prev:
        print(f"на дату {i['Date'].split('T')[0].replace('-','.')} курс ПОВЫСИЛСЯ и составил {i['Cur_OfficialRate']}")
        dynamics['up'].append({i['Date']: i['Cur_OfficialRate']})
    if i['Cur_OfficialRate'] < prev:
        print(f"на дату {i['Date'].split('T')[0].replace('-','.')} курс понизился и составил {i['Cur_OfficialRate']}")
        dynamics['down'].append({i['Date']: i['Cur_OfficialRate']})
    prev = i['Cur_OfficialRate']
print(dynamics)

# Сохраним этот словарь как JSON :
with open("dz7_dynamics.json", "w") as f:
    json.dump(dynamics, f)

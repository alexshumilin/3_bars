#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json, sys, math, os.path

if len(sys.argv) == 1:
    print("Укажите параметром запуска программы имя файла с данными о барах")
    print("Например " + sys.argv[0] + " data.json")
    exit(0)

if not os.path.exists(sys.argv[1]):
    print("Файл с данными JSON не найден. Проверьте корректность имени файла.")
    exit(0)

print("Укажите ваше местоположение в Москве, что бы найти ближайший бар:")
#   55.752283, 37.617985 Moscow centre
try:
    latitude = float(input('Введите широту (примерно от 55.53 до 55.92): '))
    longitude = float(input('Введите долготу (примерно от 37.35 до 37.87): '))
except ValueError:
    latitude = None
    longitude = None

with open(sys.argv[1], encoding='cp1251') as json_file:
    bars = json.load(json_file)

max_seats = bars[0]["SeatsCount"]
idx_biggest_bar = 0
min_seats = bars[0]["SeatsCount"]
idx_smallest_bar = 0
distance = float(180**2)    # the whole Earth
idx_nearest = 0


for bar_number, bar in enumerate(bars):
    #   print("Processing item : " + str(bar_number))
    if bar["SeatsCount"] > max_seats:
        max_seats = bar["SeatsCount"]
        idx_biggest_bar = bar_number
    if bar["SeatsCount"] < min_seats:
        min_seats = bar["SeatsCount"]
        idx_smallest_bar = bar_number
    if latitude is not None and longitude is not None:
        delta_lat = latitude - float(bar["Latitude_WGS84"])
        delta_lon = longitude - float(bar["Longitude_WGS84"])
        hypotenuse = math.sqrt(delta_lat**2 + delta_lon**2)
        if hypotenuse < distance:
            distance = hypotenuse
            idx_nearest = bar_number

print("Самый большой " + bars[idx_biggest_bar]["Name"] + " имеет " + str(bars[idx_biggest_bar]["SeatsCount"]) + " мест")
print("Самый маленький " + bars[idx_smallest_bar]["Name"] + " имеет " + str(bars[idx_smallest_bar]["SeatsCount"]) + " мест")
if latitude is not None and longitude is not None:
    print("Самый близкий к вам " + bars[idx_nearest]["Name"] + " имеет " + str(bars[idx_nearest]["SeatsCount"]) + " мест")
else:
    print("Вы указали неверные координаты, найти ближайший бар невозможно")

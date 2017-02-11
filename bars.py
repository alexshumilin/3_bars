#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json, sys, math

if len(sys.argv) == 1:
    print("Укажите параметром запуска программы имя файла с данными о барах")
    print("Например " + sys.argv[0] + " data.json")
    exit(0)

print("Укажите ваше местоположение в Москве, что бы найти ближайший бар:")
# 55.752283, 37.617985 Moscow centre
longitude = float(input('Введите долготу (примерно от 37.35 до 37.87): '))
latitude = float(input('Введите широту (примерно от 55.53 до 55.92): '))

with open(sys.argv[1], encoding='cp1251') as data_file:
    data = json.load(data_file)

max_seats = data[0]["SeatsCount"]
index_big_bar = 0
min_seats = data[0]["SeatsCount"]
index_small_bar = 0
distance = float(180**2) # the whole Earth
index_nearest = 0

# for item in data 
for i in range(len(data)):
#   print("Processing item : " + str(i + 1) + " with ID : " + data[i]["ID"])
    if data[i]["SeatsCount"] > max_seats:
        max_seats = data[i]["SeatsCount"]
        index_big_bar = i
    if data[i]["SeatsCount"] < min_seats:
        min_seats = data[i]["SeatsCount"]
        index_small_bar = i
    delta_lat = latitude - float(data[i]["Latitude_WGS84"])
    delta_lon = longitude - float(data[i]["Longitude_WGS84"])
    d = math.sqrt(delta_lat**2 + delta_lon**2)
    if d < distance:
        distance = d
        index_nearest = i

print("Самый большой " + data[index_big_bar]["Name"] + " имеет " + str(data[index_big_bar]["SeatsCount"]) + " мест")
print("Самый маленький " + data[index_small_bar]["Name"] + " имеет " + str(data[index_small_bar]["SeatsCount"]) + " мест")
print("Самый близкий к вам " + data[index_nearest]["Name"] + " имеет " + str(data[index_nearest]["SeatsCount"]) + " мест")

'''with open("weather_data.csv") as weather_file:
    data = weather_file.readlines()
    print(data)

import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
temp_list = data['temp'].to_list()
max_temp = data['temp'].max()

#Get data in columns
#print(data['condition'])
#print(data.day)

#get data in particular row
#print(data[data.day == 'Monday'])

#get data from in a row with highest temperature
#print(data[data.temp== max_temp])

#convert temp of monday to fahrenheit
monday = data[data.day == 'Monday']
monday_temp = monday.temp[0]
print(monday_temp*9/5 +32)'''

#To count the squirrel based on their colors
import pandas
datas = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = datas["Primary Fur Color"].dropna()
colors_count = {'Fur Color': ['grey', 'red', 'black'], 'Count': [0, 0, 0]}
for color in fur_colors:
    if color == 'Gray':
        colors_count['Count'][0]+=1
    elif color == 'Cinnamon':
        colors_count['Count'][1]+=1
    else:
        colors_count['Count'][2]+=1

data = pandas.DataFrame(colors_count)
data.to_csv("squirrel_count.csv")

#Method 2
import pandas
datas = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_colors = len(datas[datas["Primary Fur Color"] == 'Gray'])
red_colors = len(datas[datas["Primary Fur Color"] == 'Cinnamon'])
black_colors = len(datas[datas["Primary Fur Color"] == 'Black'])
colors_count = {
    'Fur Color': ['grey', 'red', 'black'], 
    'Count': [grey_colors, red_colors, black_colors]
}
data = pandas.DataFrame(colors_count)
data.to_csv("squirrel_count2.csv")

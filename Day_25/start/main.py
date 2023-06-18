import pandas

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if len(row[1]) <= 2:
#             temperatures.append(int(row[1]))
#
#     print(temperatures)



# data = pandas.read_csv('weather_data.csv')
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(sum(temp_list)/len(temp_list))
#
# print(data['temp'].max())
#
#
# print(data[data['temp'] == data['temp'].max()])

# create data frame
# data_dict ={
#     "students": ['Amy', 'Bartek', 'Michał'],
#     'score' : [23, 26, 66]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

red_list = data[data['Primary Fur Color'] == 'Cinnamon']['Primary Fur Color'].to_list()
black_list = data[data['Primary Fur Color'] == 'Black']['Primary Fur Color'].to_list()
gray_list = data[data['Primary Fur Color'] == 'Gray']['Primary Fur Color'].to_list()
print(red_list)
print(black_list)
print(gray_list)

data_dict={
    'Fur Color' : ['grey','red','black'],
    'Count':[len(gray_list),len(red_list),len(black_list)]
}
final_data = pandas.DataFrame(data_dict)
final_data.to_csv('new_csv.csv')
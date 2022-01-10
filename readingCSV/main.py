""" import csv

with open(f"C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/readingCSV/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print("Temperature:", temperature) """


import pandas

data = pandas.read_csv("C:/Users/rub75/OneDrive/Documents/Programmation/Python/BootcampPy2022/readingCSV/weather_data.csv")
#print(data["temp"])

""" data_dict = data.to_dict()
print(data_dict) """

data_list = data["temp"].to_list()
print(data_list)
#print("Moyenne:", round(data["temp"].mean(), 1))

def get_max(data_list: list):
    max = data_list[0]
    for i in range(len(data_list)):
        if max < data_list[i]:
            max = data_list[i]
    return max

#get_max(data_list)
#print("Max:", data["temp"].max())

#print(data[data.temp == get_max(data_list)])

temp_Mond = data[data.day == "Monday"].temp
print(temp_Mond, temp_Mond*9/5+32)
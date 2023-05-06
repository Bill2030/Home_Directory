
import pandas
data = pandas.read_csv("weather_data.csv")
#print(type(data))
#print(data["temp"])
#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data["temp"].to_list

#print(sum(temp_list))
#print(data["temp"].mean())
#print(data["temp"].median())
#print(data["temp"].max())
#Get data in columns
#print(data["condition"])
#data.condition
#print(data.condition)

# get the data in a row

#print(data[data.day == "Monday"])

#data.temp == data.temp.max()
#print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]
#print(monday.condition)
#print(temp_fer)

# Create a data Frame from scratch

#data = pandas.DataFrame(data_dict)
#print(data)
#data.to_csv("new_data")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"]=="Black"])


print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
print(data_dict)
df  = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")











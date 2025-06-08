# import csv
# import pandas as pd

# with open("weather_data.csv") as weather_data:
#     weatherlist = csv.reader(weather_data)
#     temperatures = []
#     for row in weatherlist:
#         if row[1] == "temp":
#             continue
#         temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas as pd
# from statistics import mean

# file = pd.read_csv("weather_data.csv")

# monday = file[file["day"] == "Monday"]
# mondaytemp = monday["temp"]

# mondaytempF = (mondaytemp * 9 / 5) + 32

# print(round(mondaytempF,2))

import pandas

squirrel_data = pandas.read_csv("squirrel_data.csv")
squirrel_color_count = {"Colors":["Gray","Cinnamon","Black"],"Count":[0,0,0]}

squirrel_colors = squirrel_data["Primary Fur Color"].dropna().to_list()

for squirrel in squirrel_colors:
    for colors in range(len(squirrel_color_count["Colors"])):
        if squirrel == squirrel_color_count["Colors"][colors]:
            squirrel_color_count["Count"][colors] += 1

output_csv = pandas.DataFrame(squirrel_color_count)
output_csv.to_csv("squirrelcolors.csv")
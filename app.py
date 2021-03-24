
'''Main application'''

import matplotlib.pyplot as plt
import pandas

from extract import open_file
from transform import remove_columns
from transform import yearly_average_temps
from transform import create_id
from transform import convert_type
from transform import create_dataframe

#extract raw data
raw_data = open_file()

land_and_ocean_temps = remove_columns(raw_data)

dataframe = create_dataframe(land_and_ocean_temps)

dataframe = convert_type(dataframe)

mean_yearly_temps_dataframe = yearly_average_temps(dataframe)

#create table of data with new index
mean_yearly_temps_dataframe = create_id(mean_yearly_temps_dataframe)

print(mean_yearly_temps_dataframe)

x = mean_yearly_temps_dataframe['Year']
y = mean_yearly_temps_dataframe['land temps']

plt.scatter(x,y)
plt.show()

x = mean_yearly_temps_dataframe['Year']
y = mean_yearly_temps_dataframe['ocean temps']

plt.scatter(x,y)
plt.show()

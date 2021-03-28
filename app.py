
'''Main application'''

import matplotlib.pyplot as plt

from os import system
from time import sleep

'''extract modules'''
from extract import open_file_CO2_data
from extract import open_file_global_temps 
from extract import extract_world_data

'''transform modules'''
from transform import remove_columns
from transform import create_dataframe
from transform import yearly_average_temps
from transform import create_id
from transform import convert_type
from transform import organise_co2_data
from transform import remove_null_values



'''Exracting the data into different forms from global warming temps csv'''
raw_data = open_file_global_temps()
land_and_ocean_temps = remove_columns(raw_data)
dataframe = create_dataframe(land_and_ocean_temps)
dataframe = create_dataframe(land_and_ocean_temps)
dataframe = convert_type(dataframe)
mean_yearly_temps_dataframe = yearly_average_temps(dataframe)
mean_yearly_temps_dataframe = create_id(mean_yearly_temps_dataframe)

'''Extracting data from CO2 emissions csv'''
raw_data = open_file_CO2_data() 
organised_data = organise_co2_data(raw_data)
global_data = extract_world_data(organised_data)
global_data = remove_null_values(global_data)



'''menu functions'''

def print_dataframe():
    print(mean_yearly_temps_dataframe)
    
def print_land_scatterplot():
    x = mean_yearly_temps_dataframe['Year']
    y = mean_yearly_temps_dataframe['land temps']
    plt.scatter(x,y)
    plt.show()
    
def print_ocean_scatterplot():
    x = mean_yearly_temps_dataframe['Year']
    y = mean_yearly_temps_dataframe['ocean temps']
    plt.scatter(x,y)
    plt.show()

def clear():
    system('cls')


def menu():
    menu = True
    while menu == True:
        clear()
        print('''Select one of the following options:
                
                    0) exit
                    1) land and ocean temp dataframe
                    2) land temps scatterplot
                    3) ocean temps scatterplot''')
        print()
        user = int(input('Enter option here: '))
        if user == 0:
            clear()
            menu = False
        elif user == 1:
            clear()
            print_dataframe()
        elif user == 2:
            clear()
            print_land_scatterplot()
        elif user == 3:
            clear()
            print_ocean_scatterplot()
        else:
            clear()
            print('please select a valid option')
            sleep(3)

#outputs a menu to the cli
# menu()

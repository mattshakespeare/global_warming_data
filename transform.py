'''transform data'''
import pandas as pd


#remove unwanted columns
def remove_columns(data):
    

    for row in data:
    
        del row[1]
        del row[2]
        del row[3]
        del row[4]
        del row[5]
        del row[6]
    

    return data

# convert datetime to datetime
def convert_type(data):
    
    data['date'] = pd.to_datetime(data['date'])
    
    data['land temps'] = pd.to_numeric(data['land temps'])
    
    data['ocean temps']  = pd.to_numeric(data['ocean temps'])
    
    return data
    

# create table with average yearly temps
def yearly_average_temps(data):
    
    data = data.set_index('date')
    
    year = data.index.year
    
    mean_yearly_temps = data.groupby(year).mean()
    
    return mean_yearly_temps


def create_id(data):
    
    data = data.set_index([pd.Index(x for x in range(len(data)))])
    
    #reset year column
    data['Year'] = pd.Index(x + 1750 for x in range(len(data)))
    
    
    return data

def create_dataframe(data):
    
    dataframe = pd.DataFrame(data=data)
    dataframe = dataframe.drop(0)
    
    return dataframe

def organise_CO2_data(data):
    
    del data[0]
    
    year_list = []
    for row in data[0][None]:
        if len(row) == 4:
            year_list.append(row)
    
    countries = []
    for row in data:
        if row['\ufeff"Data Source"'] not in countries:
            countries.append(row['\ufeff"Data Source"'])
    del countries[0]
    
    CO2_list = []
    for row in data:
        if row[''] == 'Total greenhouse gas emissions (kt of CO2 equivalent)':
            del row[None][0]
            CO2_list.append(row['\ufeff"Data Source"'])
            for i in range(len(year_list)):
                CO2_list.append(
                                {
                                    year_list[i]:row[None][i]
                                })
    
    for row in CO2_list:
        print(row)
                
            

    
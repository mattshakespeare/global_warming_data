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

def organise_co2_data(data):
    
    del data[0]
    
    year_list = []
    for row in data[0][None]:
        if len(row) == 4:
            year_list.append(row)
    
    co2_list = []
    for row in data:
        if row[''] == 'Total greenhouse gas emissions (kt of CO2 equivalent)':
            del row[None][0]
            co2_dict = {row['\ufeff"Data Source"'] : dict(zip(year_list,row[None]))}
            co2_list.append(co2_dict)
    
    return co2_list

def remove_null_values(data):
    
    for row in data:
        for item in row.values():
            for value in item.copy():
                if item[value] == '':
                    del item[value]
    return data

def create_co2_dataframe(data):
    
    world_data = []
    for dic in data:
        dataframe = pd.DataFrame.from_dict(data=dic, orient='columns')
    return dataframe
    
    
            
            
    
                
    
    
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

def create_co2_dataframe(data):
    
    countries = []
    data = []
    for dic in data:
        for key, values in dic.items():
            countries.append(key)
            for value in values.values():
                data.append(value)
            
    index = [i for i in range(1960,2021)]
    
    dataframe = pd.DataFrame(columns=countries, index=index, data=data)
    print(dataframe)
    
    
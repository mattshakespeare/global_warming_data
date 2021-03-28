'''extract data from csv file'''
import csv
import boto3

def open_file_CO2_data():
    
    bucket = 'myglobalwarmingdata'
    key = 'API_19_DS2_en_csv_v2_2056506.csv'
    
    s3 = boto3.client('s3')
    
    obj = s3.get_object(Bucket=bucket, Key=key)
    
    data = obj['Body'].read().decode('utf-8')
    
    csv_data = csv.DictReader(data.splitlines())
    
    csv_data_list = []
    
    for row in csv_data:
        csv_data_list.append(row)
    
    return csv_data_list

def open_file_global_temps():
    
    bucket = 'myglobalwarmingdata'
    key = 'GlobalTemperatures.csv'
    
    s3 = boto3.client('s3')
    
    obj = s3.get_object(Bucket=bucket, Key=key)
    
    data = obj['Body'].read().decode('utf-8')
    
    headers = ['date','land temps', 1,2,3,4, 'ocean temps',5,6]
    csv_data = csv.DictReader(data.splitlines(), headers)
    
    csv_list_data = []
    for item in csv_data:
        csv_list_data.append(item)

    return csv_list_data
    
## IMPORTS

import os

import pandas as pd

from pydataset import data

from env import host, username, password, sql_connexion





## FUNCTION TO CONNECT TO THE MYSQL SERVER

def sql_connexion(db, user = username, host = host, password = password):
    
    '''
    This function connects to the SQL database,
    allowing for the retrieval of remote data.
    '''
    
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
    
    
    
    
    
## FUNCTION TO ACQUIRE THE DATASET FROM SQL
    # df = dataframe
    # db = sql database

def get_data(df, db):
    
    '''
    This function retrieves Telco data either from a .csv, 
    if the .csv is held locally, or pulls it from SQL 
    in the case that it's held remotely.
    '''
    
    if os.path.isfile('file.csv'):
        
        return pd.read_csv('file.csv')
    
    else:
        
        url = df('db')
    
        query = '''
                SELECT * 
                FROM customers
                '''
        df = pd.read_sql(query, url)
        
        df.to_csv('db.csv')
        
    return df
    


   
    
## Zillow 2017 properties FUNCTION TO ACQUIRE THE DATASET FROM SQL
    

def get_zillow_data():
    
    '''
    This function retrieves Zillow 2017 data either from a .csv, 
    if the .csv is held locally, or pulls it from SQL 
    in the case that it's held remotely.
    '''
    
    file = 'zillow_single_family_properties_2017.csv'
    
    if os.path.isfile(file):
        
        return pd.read_csv(file)
    
    else:
        
        url = sql_conn('zil')
    
        query = '''
        SELECT bedroomcnt, bathroomcnt, 
        calculatedfinishedsquarefeet, 
        taxvaluedollarcnt, yearbuilt, 
        taxamount, fips, propertylandusetypeid
        FROM properties_2017
        WHERE propertylandusetypeid LIKE '261';
                '''
        zil = pd.read_sql(query, url)
        
        zil.to_csv(file)
        
    return zil
    
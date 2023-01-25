## IMPORTS

import os

import pandas as pd

from pydataset import data

from env import host, username, password, sql_connexion

from sklearn.model_selection import train_test_split



## THIS FUNCTION WILL PREPARE THE TELCO DATASET FOR USE IN ANALYSIS.

def prep_telco(df):
    
    '''
    This function serves to tidy and prepare the 
    Telco dataset for use in analysis and evaluation.
    '''
    
    ##   Drop any unnecessary, unhelpful, or duplicated columns :
    ##   payment_type_id, internet_service_type_id, contract_type_id 
    
    columns_drop = ['payment_type_id', 'internet_service_type_id','contract_type_id']
    df.drop(columns = columns_drop, axis = 1, inplace = True)
  
    
    ##     Encode the categorical columns. 
    #      Create dummy variables of the categorical columns and concatenate them onto the dataframe.
    
    dummy_df = pd.get_dummies(df[['gender','partner', 'dependents', 'paperless_billing', 'churn']])    
    
    
    ##  Concatenate the original dataframe and the dummy variables
    
    telco_df = pd.concat([df, dummy_df], axis = 1)
    
    return telco_df



## TELCO DATA TRAIN-TEST-VALIDATE.
## USES TELCO DATASET AS DEFINITION, BUT CAN TAKE IN ANY DATASET.
    
def telco_training_validate_testing(df, target = ''):
    
    '''
    This function serves to split data into training, validating
    and testing groups, allowing for machine learning-training 
    to be undertaken.
    '''
    
    seed = 27  
    
    train_telco, val_telco = train_test_split(tidied_telco, 
                                              train_size = 0.7, 
                                              random_state = seed, 
                                              stratify = tidied_telco[target])

    validate_telco, test_telco = train_test_split(val_test, 
                                                  train_size = 0.5, 
                                                  random_state = seed, 
                                                  stratify = val_test[target])
    
    return train_telco, validate_telco, test_telco 




## A GENERIC FUNCTION TO TRAIN, TEST AND SPLIT DATA.

def my_train_test_split(df, target):
    
    '''
    This is an alternate, generic function serving to split data 
    into training, validating and testing groups, allowing for 
    machine learning-training to be undertaken.
    '''
    
    train, test = train_test_split(df, test_size = .2, 
                                   random_state = 123, 
                                   stratify = df[target])
    
    train, validate = train_test_split(train, test_size = .25, 
                                       random_state = 123, 
                                       stratify = train[target])
    
    return train, validate, test



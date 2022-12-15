#These are the imports needed to run the functions within this file
import os
import pandas as pd
from sklearn.model_selection import train_test_split
#this will connect to Codeup mysql server if this function is within the env.py file in directory
from env import host, username, password

def split_train_test(df, col, seed=42):
    '''
    This function will split a dataset into train, validate, and test variables to model with. Make sure to assign to three 
    variables when running.
    '''
    seed = 123
    train, val_test = train_test_split(df, train_size=.6, random_state=123, stratify=df[col])
    validate, test = train_test_split(val_test, train_size=.6, random_state=123, stratify=val_test[col])
    
    return train, validate, test

def prep_iris(df):
    '''
    This function is used to prepare the iris dataset. It will drop several unneeded columns, rename the 'species_name' to just 
    'species', and create and concatenate dummies.
    '''
    to_drop = ['species_id', 'measurement_id', 'Unnamed: 0']
    df.drop(columns=to_drop, inplace=True)
    df = df.rename(columns={'species_name':'species'})
    
    dummies = pd.get_dummies(df[['species']], drop_first=True)
    df = pd.concat([df, dummies], axis=1)
    
    return df

def prep_titanic(df):
    '''
    This is used to prepare the titanic dataset to work with. It will drop unneeded columns, as well as create and then 
    concatenate dummies onto the DataFrame
    '''
    to_drop = ['Unnamed: 0', 'class', 'embarked', 'passenger_id', 'deck', 'age']
    df.drop(columns=to_drop, inplace=True)
    
    dummies = pd.get_dummies(df[['sex', 'embark_town']], drop_first=True)
    df = pd.concat([df, dummies], axis=1)
    
    df = df.drop(columns=['sex', 'embark_town'])
    
    return df

def prep_telco(df):
    '''
    This function will prepare the telco_churn dataset for further use. It will convert the total_charges column into the float 
    data type, create various dummies and concatenate those dummies, and then drop unneeded columns.
    '''
    telco['total_charges'] = telco['total_charges'].replace(' ', '0')
    telco['total_charges'] = telco['total_charges'].astype(float)
    
    to_dummy = ['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 
                'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 
                'paperless_billing', 'contract_type', 'internet_service_type', 
                'payment_type']
    dummies = pd.get_dummies(df[to_dummy], drop_first=True)
    df = pd.concat([df, dummies], axis=1)
    
    drop = ['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 
                'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 
                'paperless_billing', 'contract_type', 'internet_service_type', 
                'payment_type', 'Unnamed: 0', 'payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id']
    df.drop(columns=drop, inplace=True)
                 
    return df
import os
import pandas as pd
from env import host, username, password
from sklearn.model_selection import train_test_split

#function to turn a dataset into train, validate, and test subsets
def split_train_test(df, col, seed=42):
    
    seed = 123
    train, val_test = train_test_split(df, train_size=.6, random_state=123, stratify=df[col])
    validate, test = train_test_split(val_test, train_size=.6, random_state=123, stratify=val_test[col])
    
    return train, validate, test
#make sure when using this to assign three variables in the right order: train, validate, test

#function to prepare the iris dataset for use
def prep_iris(df):
    to_drop = ['species_id', 'measurement_id', 'Unnamed: 0']
    df.drop(columns=to_drop, inplace=True)
    df = df.rename(columns={'species_name':'species'})
    
    dummies = pd.get_dummies(df[['species']], drop_first=True)
    df = pd.concat([df, dummies], axis=1)
    return df

#function to prepare the titanic dataset for use
def prep_titanic(df):
    to_drop = ['Unnamed: 0', 'class', 'embarked', 'passenger_id', 'deck', 'age']
    df.drop(columns=to_drop, inplace=True)
    
    dummies = pd.get_dummies(df[['sex', 'embark_town']], drop_first=True)
    df = pd.concat([df, dummies], axis=1)
    return df

#function to prepare telco_churn dataset for use
def prep_telco(df):  
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
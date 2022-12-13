import os
import pandas as pd
from env import host, username, password
#this will connect to Codeup mysql server if this function is within the env.py file in directory


def get_connection(db, user=username, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    if os.path.isfile('titanic.csv'):
        return pd.read_csv('titanic.csv')
    else:
        url = get_connection('titanic_db')
        query = '''
                SELECT *
                FROM passengers
                '''
        titanic = pd.read_sql(query, url)
        titanic.to_csv('titanic.csv')
        return titanic

def get_iris_data():   
    if os.path.isfile('iris.csv'):
        return pd.read_csv('iris.csv')
    else:
        url = get_connection('iris_db')
        query = '''
                SELECT *
                FROM species
                JOIN measurements USING(species_id);
                '''
        iris = pd.read_sql(query, url)
        iris.to_csv('iris.csv')
        return iris

def get_telco_data():
    if os.path.isfile('telco.csv'):
        return pd.read_csv('telco.csv')
    else:
        url = get_connection('telco_churn')
        query = '''
                SELECT *
                FROM customers
                JOIN contract_types USING(contract_type_id)
                JOIN internet_service_types USING (internet_service_type_id)
                JOIN payment_types types USING(payment_type_id);
                '''
        telco = pd.read_sql(query, url)
        telco.to_csv('telco.csv')
        return telco
    
#this will return the data from specifically the attendance table in the tidy data dataset
def get_attendance_data():
    if os.path.isfile('attendance.csv'):
        return pd.read_csv('attendance.csv')
    else:
        url = get_connection('tidy_data')
        query = '''
                SELECT *
                FROM attendance
                '''
        attendance = pd.read_sql(query, url)
        attendance.to_csv('attendance.csv')
        attendance.drop(columns='Unnamed: 0.1')
        return attendance
    

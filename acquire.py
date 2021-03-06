import pandas as pd 
import numpy as np 
import os
from env import host, user, password 

#get_connect will retrieve user login info from env file to login to codeup data science database server

def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

#get_telco_data will make a connection to the sql database, read a query, and return a pandas dataframe

def get_telco_data():
     if os.path.isfile('telco_churn.csv') == False:
         sql_query = '''
                        SELECT *
                        FROM customers
                        JOIN payment_types USING(payment_type_id)
                        JOIN internet_service_types USING(`internet_service_type_id`)
                        JOIN contract_types USING(`contract_type_id`);
                    '''
         df = pd.read_sql(sql_query, get_connection('telco_churn'))
         df.to_csv('telco_churn.csv')
     else:
        df = pd.read_csv('telco_churn.csv', index_col=0)
     return df
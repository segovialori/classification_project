import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler
from acquire import get_telco_data
# ----------------------- #
#       Prepare           #
# ----------------------- #

#function to change columns from yes/no to o/1
def binary(df):
    binary_columns = ['partner', 'dependents', 'phone_service', 'paperless_billing', 'churn']
    for feature in binary_columns:
        df[feature].replace(to_replace='Yes', value=1, inplace=True)
        df[feature].replace(to_replace='No', value=0, inplace=True)
    

def prep_telco():
    df = get_telco_data()
    df.drop(columns = ['contract_type_id', 'internet_service_type_id', 'payment_type_id'], inplace=True)
    binary(df)
    add_ons = ['online_security', 'online_backup', 'tech_support', 'streaming_tv', 'streaming_movies', 'device_protection']
    df[add_ons] = df[add_ons].replace({'No': 0, 'None': 0, 'No internet service': 0, 'Yes': 1})
    df['phone_lines'] = df['multiple_lines'].replace({'No phone service': 0, 'No': 1, 'Yes': 2})
    dummy_df = pd.get_dummies(df[['internet_service_type']], dummy_na=False, drop_first=[True, True])
    df = pd.concat([df, dummy_df], axis=1)
    df.rename(columns={'internet_service_type_Fiber optic': 'fiber', 'internet_service_type_None': 'no_internet'}, inplace=True)
    df['contract'] = df[['contract_type']].replace({'Month-to-month': 0, 'One year': 1, 'Two year': 2})
    df["is_female"] = df[['gender']].replace({'Male': 0, 'Female': 1})
    df.drop(columns = ['multiple_lines', 'internet_service_type', 'contract_type'], inplace=True)
    df.drop(columns=['gender'], inplace=True)
    df.drop(columns=['payment_type'], inplace =True)
    df['total_charges'] = pd.to_numeric(df.total_charges, errors='coerce')
    df['total_charges'] = df.total_charges.fillna("0.00")
    df['tenure_years'] = round((df.tenure / 12), 2)
    df = df.set_index('customer_id')
    return df



# ----------------------- #
#       Exploration       #
# ----------------------- #
def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test



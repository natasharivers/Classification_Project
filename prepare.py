import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


###################### Prep Telco Churn Data ######################

def prep_telco_churn(df):
    '''
    This function takes in the telco_churn df acquired by get_telco_churn_data
    Returns the telco_churn df.
    '''
    # drop duplicate columns from join
    df = df.loc[:, ~df.columns.duplicated()]
    
    # change data types
    df.total_charges = df.total_charges.str.replace(' ', '0').astype(float)
    df.replace({'churn': {'No':0, 'Yes':1}}, inplace=True)
    df.replace({'partner': {'No':0, 'Yes':1}}, inplace=True)
    df.replace({'dependents': {'No':0, 'Yes':1}}, inplace=True)
    df.replace({'phone_service': {'No':0, 'Yes':1}}, inplace=True)
 
    #drop duplicates
    df.drop_duplicates(inplace=True)
    
    return df

###################### Test Train Split Telco Churn Data ######################

def train_validate_test_split(df):
    '''
    This function take in the telco_churn data from aquire.py, get_telco_churn_data(),
    performs a split, stratifies by churn.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.churn)
    return train, validate, test
    
###########################TELCO SPLIT###############################################


def telco_split(df):
    '''
    This function take in the telco_churn data from aquire.py, get_telco_churn_data(),
    performs a split, stratifies by churn.
    Returns train, validate, and test dfs.
    '''
    #split data
    train, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train, test_size=.3, random_state=123)
    return train, validate, test
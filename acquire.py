import pandas as pd 
import numpy as np 
import os
from env import host, user, password 

def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
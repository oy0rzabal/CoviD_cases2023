import pandas as pd
import numpy as np
import random
import time
import os
from pyspark import SparkContext
from utils import get_data, data_processing
from datetime import datetime
import uuid
import lxml

#Empezamos hacer la funcion de extracion de datos:
#Varibale donde se encuentra la ulr y los datos:
url = [
    'https://es.wikipedia.org/wiki/Pandemia_de_COVID-19'
]
#Casos:
casos = ['Casos']

#Creamos el dataFrame:
df_c = {
    'url':url,
}

#Creamos el dataFrame:
def df_covid():
    df_covidsw = pd.DataFrame(df_c)
    #Creamos el extractor de los datos:
    df_covids = pd.read_html(df_covidsw)
    return df_covids.head()

#df_covid = pd.read_html(df_covid)

if __name__ == '__main__':
    print(df_covid())
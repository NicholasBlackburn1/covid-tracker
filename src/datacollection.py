from covid import Covid
import numpy as np
from pandas.io.json import json_normalize 
import matplotlib as mat
import json
"""
This python class is for grabing data and organizing the data 
@author nicholas blackburn
"""
covid = Covid()

countries = covid.list_countries()

italy_cases = covid.get_status_by_country_name("italy")
usa_cases = covid.get_status_by_country_name("US")
china_cases = covid.get_status_by_country_name("china")

def getData(Location):
    json_parse = json.loads(Location)
    
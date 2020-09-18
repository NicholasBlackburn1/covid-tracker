from covid import Covid
import numpy as np
from pandas.io.json import json_normalize 
import matplotlib as mat
import json
from matplotlib import pyplot as plt
"""
This python class is for grabing data and organizing the data 
@author nicholas blackburn
"""
covid = Covid(source="worldometers")

countries = covid.list_countries()

italy_cases = covid.get_status_by_country_name("italy")
usa_cases = covid.get_status_by_country_name("USA")
china_cases = covid.get_status_by_country_name("china")

# gets Data for the graph
def getData(Location):
    print(Location)
    confirmed = Location["confirmed"]
    active = Location["active"]
    recovered = Location["recovered"]
    new = Location["new_cases"]
    deaths = Location["deaths"]
    newDeaths = Location["new_deaths"]
    population = Location["population"]
    
    print("RECOVERED",recovered)
    print("ACTIVE",active)
    print("CONFIRMED",confirmed)
    print("NEW",new)
    print("deaths",deaths)
    print("newDeaths",newDeaths)
    print("population",population)
    
    
    fig, ax = plt.subplots()
    ax.plot(confirmed, new)

    ax.set(xlabel='Confirmed cases', ylabel='Active',title='Covid Tracker By nickB')
    plt.show()
    
    
getData(Location=usa_cases)
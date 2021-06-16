import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

def load_interpolated_racesing_data():
    """Loads interpolated racesing data

    Returns:
        DataFrame(DF): DataFrame
    """    
    df = pd.read_csv('../../data/census_data/interpolated_racesing_data.csv')
    df.rename(columns={'Unnamed: 0': 'year'}, inplace=True)
    return df 


def load_prison_race_data():
    """Loads prison race data

    Returns:
        DF: race data for prison
    """    
    df = pd.read_csv('../../data/race_data.csv')
    df.drop(columns=['Unnamed: 0'], axis=1, inplace=True)
    return df 


def load_prison_birthplace_data():
    """Loads prison birthplace data, foreign countries and US states combined

    Returns:
        DF: prison foreign & state birthplace data
    """    
    foreign_data = pd.read_csv('../../data/original_data/foreign_data.csv')
    state_data = pd.read_csv('../../data/original_data/state_data.csv')
    combined = pd.concat([foreign_data, state_data])
    combined.rename(columns={'Unnamed: 0': 'location'}, inplace=True)
    return combined

def load_census_birthplace_data():
    """Loads census birthplace data (interpolated)

    Returns:
        DF: birthplace data interpolated from census 
    """    
    df = pd.read_csv('../../data/census_data/bpl_data_interpolated.csv')
    df.rename(columns={'Unnamed: 0': 'year'}, inplace=True)

    return df


def percentize_race_data(save=False): # COMBINE THIS W/ Below??? Mostly the same probably could have a boolean option and make into a single function 
    """ gets prison race data & census race data, combining them into a single dataframe showing the source, year, race, population, and the % of the population 
    that race comprised for that year, either of the census data or the prison data depending on the source

    Args:
        save (bool, optional): If save saves to csv, otherwise returns df. Defaults to False.

    Returns:
        DF: as described in function desc.
    """    
    census_data = load_interpolated_racesing_data()
    prison_data = load_prison_race_data()

    census_yrs = list(census_data['year'].unique())
    census_races = list(census_data.columns)[1:]
    prison_yrs = list(prison_data['Year'].unique())
    prison_races = list(prison_data['Race'].unique())
    result_index = list(range( (len(census_yrs)*len(census_races)) + (len(prison_yrs))*len(prison_races)) )
    result = pd.DataFrame(columns=['source', 'year', 'race', 'population', 'population_percent'], index=result_index) 

    idx = 0
    for yr in census_yrs: # maybe better done with iterrows? 
        yr_df = census_data[census_data['year'] == yr]
        yr_total_pop = yr_df.iloc[:, 1:].sum(axis=1).iloc[0]
        for race in census_races:
            population = yr_df[race].sum()
            percent = population / yr_total_pop
            result.iloc[idx] = ['census', yr, race, population, percent]
            idx += 1

    for yr in prison_yrs:
        yr_df = prison_data[prison_data['Year'] == yr]
        yr_total_pop = yr_df['Confined'].sum()
        for race in prison_races:
            population = yr_df[yr_df['Race']==race]['Confined'].sum()
            percent = population / yr_total_pop 
            result.iloc[idx] = ['prison', yr, race, population, percent]
            idx += 1




    if save:
        result.to_csv('../../data/prison_census_race_data.csv')
    else:
        return result 

def percentize_bpl_data(save=False):
    """Does the same as above, but for birthplace rather than race

    Args:
        save (bool, optional): If true saves as CSV, otherwise returns DF. Defaults to False.

    Returns:
        DF: birthplace data w/ percent added, see above function 
    """    
    prison_data = load_prison_birthplace_data()
    prison_yrs = list(prison_data.columns)[1:]
    prison_locations = list(prison_data['location'].unique())

    census_data = load_census_birthplace_data()
    census_yrs = list(census_data['year'].unique())
    census_locations = list(census_data.columns)[1:]
    result_index = list(range(len(prison_yrs) * len(prison_locations) + (len(census_yrs) * len(census_locations))))

    result = pd.DataFrame(columns=['source', 'year', 'birth_place', 'population', 'population_percent'], index=result_index) 

    idx = 0
    for yr in prison_yrs:
        yr_df = prison_data[['location', yr]]
        yr_total_pop = yr_df[yr].sum()
        for location in prison_locations:
            population = yr_df[yr_df['location'] == location][yr].sum()
            

            percent = population / yr_total_pop
            result.iloc[idx] = ['prison', yr, location, population, percent]
            idx += 1

    for yr in census_yrs: # maybe better done with iterrows? 
        yr_df = census_data[census_data['year'] == yr]
        yr_total_pop = yr_df.iloc[:, 1:].sum(axis=1).iloc[0]
        for location in census_locations:
            population = yr_df[location].sum()
            percent = population / yr_total_pop
            result.iloc[idx] = ['census', yr, location, population, percent]
            idx += 1

    if save:
        result.to_csv('../../data/prison_census_bpl_data.csv')
    return result


if __name__=="__main__":
    # df = percentize_bpl_data()
    # print(df.info())
    # print(df.head(40))

    df = pd.read_csv('../../data/original_data/foreign_data.csv')
    df.rename(columns={'Unnamed: 0': 'location'}, inplace=True)
    result_index = list(range(len(df['location'].unique())))
    result = pd.DataFrame(columns=['location', 'population'], index=result_index)
    for idx, row in df.iterrows():
        result.iloc[idx] = [row['location'], row.iloc[1:].sum()]
    
    result.sort_values('population', ascending=False, inplace=True)
    print(result.head(20))


    # TOP FOREIGN LOCATIONS  

    # 43            Mexico (old)        853
    # 29                 Germany        341
    # 35                   Italy        293
    # 34                 Ireland        279
    # 25                 England        267
    # 14                  Canada        217
    # 6                  Austria        168
    # 60                  Russia        125
    # 62                Scotland         78
    # 72                  Sweden         78
    # 28                  France         54
    # 30                  Greece         52
    # 40  Jugo-Slovakia (slavia)         31
    # 5                Australia         30
    # 73             Switzerland         26
    # 23                 Denmark         26
    # 32                 Hungary         22
    # 50                  Norway         19
    # 54                  Poland         19
    # 38                   Japan         16

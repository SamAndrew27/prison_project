import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

def load_interpolated_racesing_data():
    df = pd.read_csv('../../data/census_data/interpolated_racesing_data.csv')
    df.rename(columns={'Unnamed: 0': 'year'}, inplace=True)
    return df 


def load_prison_race_data():
    df = pd.read_csv('../../data/race_data.csv')
    df.drop(columns=['Unnamed: 0'], axis=1, inplace=True)
    return df 


def percentize_data(save=False):
    census_data = load_interpolated_racesing_data()
    prison_data = load_prison_race_data()

    census_yrs = list(census_data['year'].unique())
    census_races = list(census_data.columns)[1:]
    prison_yrs = list(prison_data['Year'].unique())
    prison_races = list(prison_data['Race'].unique())
    result_index = list(range( (len(census_yrs)*len(census_races)) + (len(prison_yrs))*len(prison_races)) )
    result = pd.DataFrame(columns=['source', 'year', 'race', 'population', 'population_percent',], index=result_index) 

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


if __name__=="__main__":
    percentize_data(True)
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression


# combine below into fewer functions? 


def load_data(remove_unused_samples=True, only_racesing=True, only_bpl=False, only_black=False):
    df = pd.read_csv('../../data/census_data/sample_census_data_1870-1940_aggregated_weighted.csv')
    df.drop(['Unnamed: 0'], axis=1, inplace=True)

    if remove_unused_samples:
        for sample in ['1870 1%', '1880 1%', '1900 5%', '1900 1%', '1910 1%',  '1930 5%']:
            df = df[df['sample'] != sample ]
    if only_racesing:
        df = df[df['column'] == 'RACESING']
    else:
        if only_bpl:
            df = df[df['column'] == 'BPL']

    if only_black:
        df = df[df['variable'] == 'Black']
    return df


def interpolate_black_data():
    df = load_data(True,True, False, True)
    yr_range = list(range(1870,1941))
    all_year_series = pd.Series(index=yr_range)

    for idx, row in df.iterrows():
        all_year_series.loc[row['year']] = row['population']



    all_year_series.interpolate(method='linear', inplace=True)
    return all_year_series


def interpolate_all_racesing_data(save=False):
    df = load_data(True, True, False, False)
    yr_range = list(range(1870,1941))
    races = list(df['variable'].unique())
    result_df = pd.DataFrame(columns = races, index=yr_range, dtype='float')
    races.remove('Other race, non-Hispanic')
    for idx, row in df.iterrows():
        result_df.loc[row['year'], row['variable']] = row['population']
    for race in races:
        result_df[race].interpolate(method='linear', inplace=True)
    if save:
        result_df.to_csv('../../data/census_data/interpolated_racesing_data.csv')
    else:
        return result_df

def interpolate_all_bpl_data(save=False): # probably should just be combined w/ the above function 
    df = load_data(True, False, True, False)
    yr_range = list(range(1870,1941))
    birth_places = list(df['variable'].unique())
    result_df = pd.DataFrame(columns = birth_places, index=yr_range, dtype='float')
    for idx, row in df.iterrows():
        result_df.loc[row['year'], row['variable']] = row['population']
    for bpl in birth_places:
        first_index = result_df[bpl].first_valid_index()
        last_index = result_df[bpl].last_valid_index()

        result_df.loc[first_index:last_index, bpl] = result_df.loc[first_index:last_index, bpl].interpolate(method='linear')
    if save:
        result_df.to_csv('../../data/census_data/bpl_data_interpolated.csv')
    else:
        return result_df

if __name__=="__main__":
    # df = interpolate_all_bpl_data()
    # print(df.info())
    # print(df.head(30))
    # print(df.columns)
    # df.to_csv('test.csv')
    # print(df['Missouri'].isna().sum())
    interpolate_all_bpl_data(True)


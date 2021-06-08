import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression

def load_data(remove_unused_samples=True, only_racesing=True, only_black=True):
    df = pd.read_csv('../../data/census_data/sample_census_data_1870-1940_aggregated_weighted.csv')
    df.drop(['Unnamed: 0'], axis=1, inplace=True)

    if remove_unused_samples:
        for sample in ['1870 1%', '1880 1%', '1900 5%', '1900 1%', '1910 1%',  '1930 5%']:
            df = df[df['sample'] != sample ]
    if only_racesing:
        df = df[df['column'] == 'RACESING']
    if only_black:
        df = df[df['variable'] == 'Black']
    return df


def interpolate_black_data():
    df = load_data(True,True,True)
    yr_range = list(range(1870,1941))
    all_year_series = pd.Series(index=yr_range)

    for idx, row in df.iterrows():
        all_year_series.loc[row['year']] = row['population']



    all_year_series.interpolate(method='linear', inplace=True)
    return all_year_series


def interpolate_all_racesing_data(save=False):
    df = load_data(True, True, False)
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



if __name__=="__main__":

    # interpolate_all_racesing_data(True)
    df = pd.read_csv('../../data/census_data/interpolated_racesing_data.csv')
    df.rename(columns={'Unnamed: 0': 'year'}, inplace=True)
    print(df.head())
    print(df.info())
    year_80 = df[df['year'] == 1880]
    print(year_80['Black'] / year_80.sum(axis=1))



    # df = load_data(True,True, False)
    # print(df['variable'].unique())
    # df = interpolate_all_racesing_data()
    # print(df.info())

    # print(df.iloc[:, 4])
    # white = df['White']
    # print(white)
    # df['White'] = df['White'].interpolate(method='linear')
    # print(df['White'].interpolate(method='linear', axis=0))
    # print(df.info())
    # print(df.head())


    # df = load_data(True,True,False)
    # print(df.info())
    # print(df['variable'].unique())


    # df = load_data(True, True, True)
    # print(df.info())
    
    # print(df.head(30))
    # print(df['variable'].unique())
    # X = np.array(df['year']).reshape(-1,1)
    # y = np.array(df['population'])
    # yr_range = np.array(range(1870, 1941)).reshape(-1,1)
    # lr = LinearRegression().fit(X, y)
    # pred = lr.predict(yr_range)


    # fig, ax = plt.subplots()
    # ax.scatter(X, y, color='red')
    # ax.plot(yr_range, pred)
    # plt.show()
import pandas as pd 

def create_race_df(save=False):
    df = pd.read_csv('../../data/original_data/race_data.csv')
    years = list(df.columns)[1:]
    races = list(df['Race'].unique())
    result_idx = list(range(len(years) * len(races)))
    result = pd.DataFrame(columns = ['Year', 'Race', 'Confined'], index= result_idx)
    idx = 0
    for year in years:
        for num, race in zip(df[year], races):
            result.iloc[idx] = [int(year), race, num]
            idx += 1
    if save:
        result.to_csv('../../data/race_data.csv')
    else:
        return result 


if __name__=="__main__":
    # df = pd.read_csv('../../data/original_data/race_data.csv')
    # races = list(df['Race'].unique())
    # yrs = list(df.columns)[1:]
    # print(races)
    # df = create_race_df()
    # print(df.info())
    # print(df)
    create_race_df(True)
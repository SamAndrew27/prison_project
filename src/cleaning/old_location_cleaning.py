import pandas as pd 


def load_location_data_and_clean(states = True, save=False):
    if states:
        df = pd.read_csv('../../data/state_data.csv')
        save_local = '../../data/state_data_cleaned.csv'
    else: 
        df = pd.read_csv('../../data/foreign_data.csv')
        save_local = '../../data/foreign_data_cleaned.csv'

    df = df.rename(columns={'Unnamed: 0':'location'})
    year_df = df.iloc[:, 1:]
    yrs = list(year_df.columns)

    output_idx = list(range(len(yrs) * len(df['location'].unique())))
    result = pd.DataFrame(columns=['Location', 'Year', 'Prisoners'], index= output_idx) # stupid way to index and add, do something better 


    index = 0
    for idx, row in df.iterrows():
        location = row['location']
        for yr in yrs:
            total = row[yr]
            if total == None:
                total = 0
            result.iloc[index] = [location, yr, total]
            index += 1
    result = result.fillna(0)

    if states:
        result = result.rename(columns={'Location': 'State'})
    else:
        result = result.rename(columns={'Location': 'Country'})

    if save:
        result.to_csv(save_local)
    else:
        return result




if __name__=="__main__":
    # load_location_data_and_clean(True, True)
    load_location_data_and_clean(True, True)
    load_location_data_and_clean(False, True)

    # df = df[df.Location == 'Colorado']
    # print(df)
    # for idx, row in df.iterrows()
    # df = df.iloc[:, 1:]
    # print(list(df.columns))
    # print(df.info())
    # load_state_data_and_clean(True)


    # df = pd.read_csv('../../data/state_data.csv')
    # df = df.rename(columns={'Unnamed: 0':'state'})
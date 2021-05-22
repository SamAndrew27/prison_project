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


def modernized_foreign_data(save=False): # see how this works in Tableau then considering changing country names more
    df = pd.read_csv('../../data/foreign_data_modernized.csv')

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
    if save:
        result.to_csv('../../data/foreign_data_modernized_cleaned.csv')
    else:
        return result

if __name__=="__main__":
    # df = modernized_foreign_data()
    # print(df.info())
    # print(df.head())
    modernized_foreign_data(True)
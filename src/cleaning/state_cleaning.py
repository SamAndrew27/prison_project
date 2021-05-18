import pandas as pd 


def load_state_data_and_clean(save=False):
    df = pd.read_csv('../../data/state_data.csv')
    df = df.rename(columns={'Unnamed: 0':'state'})
    result = pd.DataFrame(columns=['State', 'Year', 'Prisoners'], index= list(range(10000))) # stupid way to index and add, do something better 
    year_df = df.iloc[:, 1:]
    yrs = list(year_df.columns)

    index = 0
    for idx, row in df.iterrows():
        state = row['state']
        for yr in yrs:
            total = row[yr]
            if total == None:
                total = 0
            result.iloc[index] = [state, yr, total]
            index += 1
    result = result.dropna()

    if save:
        result.to_csv('../../data/state_data_cleaned.csv')
    else:
        return result




    return df 
if __name__=="__main__":
    load_state_data_and_clean(True)
    # df = load_state_data_and_clean()
    # for idx, row in df.iterrows()
    # df = df.iloc[:, 1:]
    # print(list(df.columns))
    # print(df.info())
    # load_state_data_and_clean(True)


    # df = pd.read_csv('../../data/state_data.csv')
    # df = df.rename(columns={'Unnamed: 0':'state'})
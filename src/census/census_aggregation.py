import pandas as pd 

def load_cleaned_data(sample_set=True):
    """Loads cleaned census data

    Args:
        sample_set (bool, optional): If True uses a smaller subset of data, otherwise uses entire dataset. Use sample for testing. Defaults to True.

    Returns:
        DataFrame: DataFrame
    """    
    if sample_set:
        df = pd.read_csv('../../data/census_data/sample_census_data_1870-1940_cleaned.csv')
    else:
        df = pd.read_csv('../../data/census_data/census_data_1870-1940_cleaned.csv')
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    return df



def variable_counts(sample_set=True, weights=True, save = False, filename='variable_counts'): # could I just be doing groupby for all of this?
    """Gets the counts of each variable for each year

    Args:
        sample_set (bool, optional): If True will denote the sample the record was drawn from. Defaults to True. - Probably shouldn't even be an option not to include this. 
        weights (bool, optional): If Weights the weights from PERWT are applied. Might as well always apply these, but for flat samples PERWT is irrelevant. Defaults to True.
        save (bool, optional): If True saves as CSV, otherwise returns pandas DF. Defaults to False.
        filename (str, optional): Name to save CSV file of in the case that 'save' is set to True. Defaults to 'variable_counts'.

    Returns:
        DataFrame: DataFrame with variables summed (and possibly weighted)
    """    
    df = load_cleaned_data(sample_set)
    years = list(df['YEAR'].unique())
    idx = 0
    race_counts = {}
    raced_counts = {}
    racesing_counts = {}
    racesingd_counts = {}
    bpl_counts = {}
    bpld_counts = {}
    nativity_counts = {}
    dict_list = [race_counts, raced_counts, racesing_counts, racesingd_counts, bpl_counts, bpld_counts, nativity_counts]
    column_names = ['RACE', 'RACED', 'RACESING', 'RACESINGD', 'BPL', 'BPLD', 'NATIVITY']
    for _, row in df.iterrows():
        if sample_set:
            sample = row['SAMPLE_cleaned']
        year = row['YEAR']
        race = row['RACE_cleaned']
        raced = row['RACED_cleaned']
        racesing = row['RACESING_cleaned']
        racesingd = row['RACESINGD_cleaned']
        bpl = row['BPL_cleaned']
        bpld = row['BPLD_cleaned']
        nativity = row['NATIVITY_cleaned']
        variable_list = [race, raced, racesing, racesingd, bpl, bpld, nativity]
        for idx, (variable, dic) in enumerate(zip(variable_list, dict_list)):
            col = column_names[idx]
            if sample_set:
                var_id = f'{variable}:{col}:{year}:{sample}'
            else:
                var_id = f'{variable}:{col}:{year}'
            if weights:
                perwt = row['PERWT']
            else:
                perwt = 1
            if var_id in dic:
                dic[var_id] += 1 * perwt
            else:
                dic[var_id] = 1 * perwt

    idx_len = 0
    for dic in dict_list:
        idx_len += len(dic)
    
    if sample_set:
        results = pd.DataFrame(columns=['variable', 'column', 'year', 'sample', 'population'], index= list(range(idx_len)))
    else:
        results = pd.DataFrame(columns=['variable', 'column', 'year', 'population'], index= list(range(idx_len)))
    
    idx = 0
    for dic in dict_list:
        for key, value in dic.items():
            split_key = key.split(':')
            if sample_set:
                results.iloc[idx] = [split_key[0], split_key[1], split_key[2], split_key[3], value]
            else:
                results.iloc[idx] = [split_key[0], split_key[1], split_key[2], value]
            idx += 1
    if save:
        results.to_csv(f'../../data/{filename}.csv')
    else:
        return results

if __name__=="__main__":
    df = load_cleaned_data()
    print(df.info())
    # df = df[['YEAR', ]]
    # print(df['PERWT'].value_counts())

    # variable_counts(sample_set=True, weights=True, save=True, filename='sample_census_data_1870-1940_aggregated_weighted')
    # variable_counts(sample_set=False, save=True, filename='census_data_1870-1940_aggregated')


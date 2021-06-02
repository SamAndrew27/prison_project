import pandas as pd 

def load_cleaned_data(sample_set=True):
    if sample_set:
        df = pd.read_csv('../../data/sample_census_data_1870-1940_cleaned.csv')
    else:
        df = pd.read_csv('../../data/census_data_1870-1940_cleaned.csv')
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    return df



def variable_counts(sample_set=True, save = False, filename='variable_counts'):
    df = load_cleaned_data(sample_set)
    years = list(df['YEAR'].unique())
    idx = 0
    race_counts = {}
    raced_counts = {}
    bpl_counts = {}
    bpld_counts = {}
    nativity_counts = {}
    dict_list = [race_counts, raced_counts, bpl_counts, bpld_counts, nativity_counts]

    for _, row in df.iterrows():
        if sample_set:
            sample = row['SAMPLE_cleaned']
        year = row['YEAR']
        race = row['RACE_cleaned']
        raced = row['RACED_cleaned']
        bpl = row['BPL_cleaned']
        bpld = row['BPLD_cleaned']
        nativity = row['NATIVITY_cleaned']
        variable_list = [race, raced, bpl, bpld, nativity]
        for variable, dic in zip(variable_list, dict_list):
            if sample_set:
                var_id = f'{variable}:{year}:{sample}'
            else:
                var_id = f'{variable}:{year}'
            if var_id in dic:
                dic[var_id] += 1
            else:
                dic[var_id] = 1

    idx_len = 0
    for dic in dict_list:
        idx_len += len(dic)
    
    if sample_set:
        results = pd.DataFrame(columns=['variable', 'year', 'sample', 'population'], index= list(range(idx_len)))
    else:
        results = pd.DataFrame(columns=['variable', 'year', 'population'], index= list(range(idx_len)))
    
    idx = 0
    for dic in dict_list:
        for key, value in dic.items():
            split_key = key.split(':')
            if sample_set:
                results.iloc[idx] = [split_key[0], split_key[1], split_key[2], value]
            else:
                results.iloc[idx] = [split_key[0], split_key[1], value]
            idx += 1
    if save:
        results.to_csv(f'../../data/{filename}.csv')
    else:
        return results

if __name__=="__main__":
    # df = load_cleaned_data()
    # print(df.info())
    variable_counts(sample_set=True, save=True, filename='sample_census_data_1870-1940_aggregated_no_weighting')
    variable_counts(sample_set=False, save=True, filename='census_data_1870-1940_aggregated')

    # variable_counts(sample_set=False, save=True, filename='sample_data_aggregates_no_weighting_used')

    # results = variable_counts(sample_set=True, save=True, filename='sample_data_aggregates_no_weighting_used')
    # print(results.info())
    # print(results.head())
    # print(race)
    # print(raced)

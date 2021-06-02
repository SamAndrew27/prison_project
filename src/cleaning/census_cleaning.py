import pandas as pd
from sklearn.model_selection import train_test_split
def create_sample(size=.01, save=True, name='sub_sample_census_data'):
    df = pd.read_csv('../../data/original_data/entire_census_dataset.csv')
    train, test = train_test_split(df, test_size=size)
    if save:
        test.to_csv(f'../../data/{name}.csv')
    else:
        return test

def load_and_clean(sample=True, drop_cols=True):
    if sample:
        df = pd.read_csv('../../data/sub_sample_census_data.csv') 
    else:
        df = pd.read_csv('../../data/original_data/entire_census_dataset.csv')
    codes = pd.read_csv('../../data/original_data/IPUMS_codes.csv')

    
    return df, codes
if __name__=="__main__":
    df, codes = load_and_clean()

    for variable in codes.Variable.unique():
        code_dict = {}
        var_codes = codes[codes['Variable'] == variable]
        for idx, row in var_codes.iterrows():
            code_dict[row['Code']] = row['Label']
        df[f'{variable}_cleaned'] = df[variable].apply(lambda x: code_dict[x])
    print(df.info())
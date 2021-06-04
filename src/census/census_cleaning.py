import pandas as pd
from sklearn.model_selection import train_test_split
def create_sample(sample_set= True, size=.01, save=True, filename='Default'):

    if sample_set:
        df = pd.read_csv('../../data/original_data/sample_census_data_1870-1940.csv')
        if filename == 'Default':
            file = 'sample_census_data_1870-1940_sub_sample'
        else:
            file = filename


    else:
        df = pd.read_csv('../../data/original_data/census_data_1870-1940.csv')
        if filename == 'Default':
            file = 'census_data_1870-1940_sub_sample'
        else:
            file = filename

    train, test = train_test_split(df, test_size=size)
    if save:
        test.to_csv(f'../../data/{file}.csv')
    else:
        return test

def load_and_clean(sample_set = True, sub_sample=True, drop_unused_cols=True, drop_reformatted_cols=True, save=False, filename='Default'):
    if sample_set:
        if sub_sample:
            df = pd.read_csv('../../data/census_data/sample_census_data_1870-1940_sub_sample.csv') 
            df.drop(['Unnamed: 0'],axis=1,inplace=True)
        else:
            df = pd.read_csv('../../data/original_data/sample_census_data_1870-1940.csv')
        if filename == 'Default':
            file = 'sample_census_data_1870-1940_cleaned'
        else:
            file = filename

    else: 

        if sub_sample:
            df = pd.read_csv('../../data/census_data/census_data_1870-1940_sub_sample.csv') 
            df.drop(['Unnamed: 0'],axis=1,inplace=True)
        else:
            df = pd.read_csv('../../data/original_data/census_data_1870-1940.csv')
        if filename == 'Default':
            file = 'census_data_1870-1940_cleaned'
        else:
            file = filename
            
    codes = pd.read_csv('../../data/original_data/IPUMS_codes.csv')
    if sample_set == False:
        codes = codes[codes['Variable'] != 'SAMPLE']

    for variable in codes['Variable'].unique():
        code_dict = {}
        var_codes = codes[codes['Variable'] == variable]
        for idx, row in var_codes.iterrows():
            code_dict[row['Code']] = row['Label']
        df[f'{variable}_cleaned'] = df[variable].apply(lambda x: code_apply(x, code_dict))
        if drop_reformatted_cols:
            df.drop([variable], axis=1, inplace=True)
    
    if drop_unused_cols and sample_set:
        df.drop(['SERIAL', 'STATEFIP'], axis=1, inplace=True)

    if drop_unused_cols and sample_set==False: # for sample sets
        df.drop(['SAMPLE', 'SERIAL', 'HHWT', 'CLUSTER', 'STATEFIP', 'PERNUM', 'PERWT', 'HISTID'], axis=1, inplace=True)


    if save:
        df.to_csv(f'../../data/{file}.csv')
    else:
        return df

def code_apply(x, code_dict):
    if pd.isnull(x):
        return x
    else:
        return code_dict.get(x, 'Unmatched Code')
def find_unmatched(sample_set=True, drop_unused_cols=True, sub_sample=False): # Iteration most likely unecessary, I think just doing value counts would suffice, no?
    df = load_and_clean(sample_set=sample_set, drop_unused_cols=drop_unused_cols,  sub_sample=sub_sample, drop_reformatted_cols=False)
    unmatched_counts = {}
    unmatched_codes = set()
    cleaned_cols = []
    for col in df.columns:
        if 'cleaned' in col:
            cleaned_cols.append(col)
    for idx, row in df.iterrows(): 
        for col in cleaned_cols:
            if row[col] == 'Unmatched Code':
                original_col = col.replace('_cleaned', '')
                unmatched_codes.add(f'{original_col}:{row[original_col]}')
                if original_col in unmatched_counts:
                    unmatched_counts[original_col] += 1
                else:
                    unmatched_counts[original_col] = 1
    return unmatched_counts, unmatched_codes
                


if __name__=="__main__":

    print('TEST 1: \n')
    c1, u1 = find_unmatched(True, True, False)
    print('TEST 2: \n')
    c2, u2 = find_unmatched(True, True, True)
    print('TEST 3: \n')
    c3, u3 = find_unmatched(False, True, False)
    print('TEST 4: \n')
    c4, u4 = find_unmatched(False, True, True)


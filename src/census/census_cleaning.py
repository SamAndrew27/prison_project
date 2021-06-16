import pandas as pd
from sklearn.model_selection import train_test_split
def create_sample(sample_set= True, size=.01, save=True, filename='Default'):
    """Creates subsample to troubleshoot with of census data (cus the census data is quite large)

    Args:
        sample_set (bool, optional): If True uses the sample census data, as distributed by IPUMS. Defaults to True.
        size (float, optional): Size of sample relative to original data. Defaults to .01.
        save (bool, optional): If True saves as csv, otherwise returns DF. Defaults to True.
        filename (str, optional): Filename to be used if 'save' set to true - if unadjusted will use default file names. Defaults to 'Default' - which uses preloaded filenames

    Returns:
        DF: subsample of census data
    """    

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
    """Loads census data in original format, removes unused columns, & replaces variable codes w/ variable names

    Args:
        sample_set (bool, optional): If True loads sample sets, otherwise loads original census records. Defaults to True.
        sub_sample (bool, optional): If True loads a subsample of data, otherwise uses entire dataset. Defaults to True.
        drop_unused_cols (bool, optional): Drops the columns we have decided to ignore for now. Defaults to True.
        drop_reformatted_cols (bool, optional): Drops columns w/ codes reformatted to show what they actually represent. Defaults to True.
        save (bool, optional): If True saves df as CSV, otherwise returns DF. Defaults to False.
        filename (str, optional): Name of file if file is saved - if nothing input uses preloads. Defaults to 'Default'.

    Returns:
        DF: cleaned census data
    """    
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
    """Replaces code with what it represents

    Args:
        x : original code
        code_dict (dict): codes as keys, value of codes as values

    Returns:
        string: what the code represents
    """    
    if pd.isnull(x):
        return x
    else:
        return code_dict.get(x, 'Unmatched Code')


def find_unmatched(sample_set=True, drop_unused_cols=True, sub_sample=False): # Iteration most likely unecessary, I think just doing value counts would suffice, no?
    """Finds unmatched codes for each column 

    Args:
        sample_set (bool, optional): If True loads sample sets, otherwise loads original census records. Defaults to True.
        drop_unused_cols (bool, optional): Drops the columns we have decided to ignore for now. Defaults to True.
        sub_sample (bool, optional): If True loads a subsample of data, otherwise uses entire dataset. Defaults to True.

    Returns:
        unmatched_counts (dict): dictionary containing the count of unmatched columns in each cleaned column
        unmatched codes (set): codes which are unmatched
    """
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


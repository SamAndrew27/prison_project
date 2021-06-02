import pandas as pd 

def load_1900():
    df = pd.read_csv('../../data/original_data/census_data_1900.csv')
    return df

def codes_to_string(df, drop_cols=False):
    codes = pd.read_csv('../../data/original_data/BPL_codes.csv')
    code_dict = {}
    for idx, row in codes.iterrows():
        code_dict[row['Code']] = row['Location']

    df['group_quarter_status'] = df['GQ'].apply(lambda x: gq_apply(x))
    df['race'] = df['RACE'].apply(lambda x: race_apply(x))
    df['racesing'] = df['RACESING'].apply(lambda x: racesing_apply(x))

    df['hispanic'] = df['HISPAN'].apply(lambda x: hispan_apply(x))
    df['birthplace'] = df['BPL'].apply(lambda x: code_dict[x])

    if drop_cols:
        df.drop(['GQ', 'RACE'], axis=1, inplace=True)
    return df


def gq_apply(x):
    if x == 1:
        return 'Households Under 1970 Definition'
    elif x == 2:
        return 'Additional Households Under 1990 Definition'
    elif x == 3:
        return 'Institutions'
    elif x == 4:
        return 'Other Group Quarters'

def race_apply(x):
    if x == 1:
        return 'White'
    elif x == 2:
        return 'Black/African American/Negro'
    elif x == 3:
        return 'American Indian or Alaska Native'
    elif x == 4:
        return 'Chinese'
    elif x == 5:
        return 'Japanese'
def racesing_apply(x):
    if x == 1:
        return 'White'
    elif x == 2:
        return 'Black'
    elif x == 3:
        return 'American Indian/Alaska Native'
    elif x == 4:
        return 'Asian and/or Pacific Islander'

def hispan_apply(x):
    if x == 0:
        return 'Not Hispanic'
    elif x == 1:
        return 'Mexican'
    elif x == 3:
        return 'Cuban'
    elif x == 4:
        return 'Other'

def bpl_apply(x, code_dict):
    return code_dict[x]
if __name__=="__main__":
    df = load_1900()
    print(df.columns)
    # print(df.BPL.unique())

    # df = codes_to_string(df)
    # print(df.info())
    # print(df.BPL.value_counts())
    # print(df.birthplace.value_counts())
    # print(len(list(df.birthplace.unique())))
    # print(len(list(df.BPL.unique())))

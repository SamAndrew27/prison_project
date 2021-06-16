
import pandas as pd 

def clean_all_first_half():
    """Loads data and legend, applies cleaning functions to df

    Returns:
        DataFrame: DataFrame w/ data cleaned
    """    
    df = load_data_or_legend(True)
    legend = load_data_or_legend(False)
    df = clean_term(df, legend)
    df = clean_crime(df, legend)
    df = clean_nativity(df, legend)
    df = clean_race(df, legend)
    df['race_adjusted'] = df['clean_race'].apply(lambda x: race_adjusted_apply(x))
    df['nativity_no_states'] = df['clean_nativity'].apply(lambda x: nat_no_states(x, legend))
    return df 

def load_data_or_legend(data=True):
    """Loads legend or data

    Args:
        data (bool, optional): If True loads data, if False loads legend. Defaults to True.

    Returns:
        DataFrame: Legend or Data
    """    
    if data:
        df = pd.read_csv('../../data/original_data/1878-1888_DATA.csv')
        return df
    else:
        legend = pd.read_csv('../../data/original_data/1878-1888_LEGEND.csv')
        return legend


def clean_term(df, legend):
    """Cleans Term data, saves to new column 'term_clean'

    Returns:
        DataFrame: w/ additional column of cleaned data
    """    
    dic = {}
    tl = legend['Term Legend'].dropna()
    for elem in tl:
        elem = elem.strip()
        temp = elem.split(':')
        dic[temp[0]] = temp[1].strip()
    df['term_clean'] = df['Term'].apply(lambda x: clean_term_apply(x, dic))
    return df
    
    
def clean_term_apply(x, dic):
    """Apply function for term cleaning

    Args:
        x (str): Term
        dic (dict): dictionary of legend terms

    Returns:
        list: list of term
    """    
    x = x.strip()
    if x in dic:
        x = dic[x]
        return [x]
    else:
        if '-' in x:
            result = []
            x = x.split('-')
            for elem in x:
                elem = elem.strip()
                if elem == 'L':
                    result.append('Life')
                else:
                    result.append(float(elem))
            return result
        else:
            if x == '?':
                return x 
            else:
                return [float(x)]


def clean_crime(df, legend):
    """cleans crime column

    Returns:
        DataFrame: Dataframe with 'crime_clean' added
    """    
    dic = {}
    for elem in legend['Crime Legend'].dropna():
        elem = elem.split(':')
        dic[elem[0]] = elem[1].strip()
    df['crime_clean'] = df['Crime'].apply(lambda x: clean_crime_apply(x, dic))
    return df
    
def clean_crime_apply(x,dic):
    """Apply function for crime

    Args:
        x (str): crime
        dic (dict): dictionary of crime legend

    Returns:
        str: type of crime
    """    
    if '(' in x:
        cutoff = x.index('(')
        x = x[:cutoff]
    x = x.split('&')
    result = []
    for elem in x:
        s_elem = elem.strip()
        if s_elem in dic:
            result.append(dic[s_elem])
        else:
            result.append(s_elem)

    return result


def clean_nativity(df, legend):
    """ cleans nativity column

    Args:
        df (DataFrame): DataFrame uncleaned
        legend (DataFrame): Legend for Data

    Returns:
        DataFrame: DataFrame w/ nativity cleaned
    """    
    dic = {} 
    for elem in legend['Countries Legend'].dropna():
        elem = elem.split(':')
        dic[elem[0]] = elem[1].strip()
    
    state_df = pd.DataFrame({'State Abbreviations': legend['State Abbreviations'], 'State Names': legend['State Names']}).dropna()
    for idx, row in state_df.iterrows():
        dic[row['State Abbreviations']] = row['State Names']

    df['clean_nativity'] = df['Nativity'].apply(lambda x: clean_nativity_apply(x, dic))
    return df 

def clean_nativity_apply(x, dic):
    """Apply function for nativity

    Args:
        x (string): original nativity
        dic (dict): dictionary w/ legend loaded

    Returns:
        string: nativity cleaned 
    """    
    x = x.strip()
    if x in dic:
        return dic[x]
    else:
        return x 

def clean_race(df, legend):
    """ cleans race column

    Args:
        df (DataFrame): DataFrame uncleaned
        legend (DataFrame): Legend for Data

    Returns:
        DataFrame: DataFrame w/ race cleaned
    """    
    dic = {} 
    for elem in legend['Race Legend'].dropna():
        elem = elem.split(':')
        dic[elem[0]] = elem[1].strip()
    
    df['clean_race'] = df['Race'].apply(lambda x: clean_race_apply(x, dic))
    return df

def clean_race_apply(x, dic):
    """Apply function for race

    Args:
        x (string): original race
        dic (dict): dictionary w/ legend loaded

    Returns:
        string: race cleaned 
    """    
    x = x.strip()
    if x in dic:
        return dic[x]
    else:
        return x

def race_adjusted_apply(x):
    """apply function for race - making a few classifications slightly less racist/antiquated 

    Args:
        x (str): race

    Returns:
        str: race
    """    
    if x == 'Mulatto':
        return 'Black'
    if x == 'Mongolian':
        return 'Asian'
    else:
        return x

def nat_no_states(x, legend):
    """replaces state names with 'United States'

    Args:
        x (str): nativity
        legend (DataFrame): Legend for Data

    Returns:
        DataFrame: DataFrame w/ states converted
    """    
    if x in list(legend['State Names'].dropna()):
        return 'United States'
    else:
        return x

if __name__=="__main__":
    pass
    # df= clean_crime()
    # vc = df.crime_clean.value_counts()

    # print(result)
    # df = load_data_or_legend(False)
    # print(df.info())
    # df = clean_race()
    # vc = df['clean_race'].value_counts()
    # vc = list(vc.index)
    
    # result = set()
    # for elem in vc:
    #     result.add(elem)
    # print(result)
    # df = clean_all_first_half()
    # print(df.info())
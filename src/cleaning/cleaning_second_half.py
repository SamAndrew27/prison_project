import pandas as pd 
def load_data_or_legend(data=True):
    """Loads legend or data

    Args:
        data (bool, optional): If True loads data, if False loads legend. Defaults to True.

    Returns:
        DataFrame: Legend or Data
    """    
    if data:
        df = pd.read_csv('../../data/1890-1900_DATA.csv')
        return df
    else:
        legend = pd.read_csv('../../data/1890-1900_LEGEND.csv')
        return legend


def clean_term(df, legend):
    """Cleans Term data, saves to new column 'term_clean'

    Returns:
        DataFrame: w/ additional column of cleaned data
    """    
    dic = {}
    tl = legend['Term Legend'].dropna()
    for elem in tl:
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
        list: list of term(s)
    """    
    x = x.strip()
    if x in dic:
        x = dic[x]
        return [x]
    else:
        if '-' in x:
            x = x.split('-')
            for elem in x:
                if elem == 'L':
                    elem = 'Life'
                else:
                    elem = float(elem.strip())
            return x 
        else:
            if x == '?':
                return None 
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



def clean_nationality(df, legend):
    dic = {} 
    for elem in legend['Nationality Legend'].dropna():
        elem = elem.split(':')
        dic[elem[0]] = elem[1].strip()

    df['clean_nationality'] = df['Nationality'].apply(lambda x: clean_nationality_apply(x, dic))
    return df 

def clean_nationality_apply(x, dic):
    x = x.strip()
    if x in dic:
        return dic[x]
    else:
        return x 


def create_race(df):
    

if __name__=="__main__":
    df = load_data_or_legend()
    legend = load_data_or_legend(False)

    df = clean_nationality(df, legend)
    vc = df['clean_nationality'].value_counts()
    vc = list(vc.index)
    
    result = set()
    for elem in vc:
        result.add(elem)
    print(result)

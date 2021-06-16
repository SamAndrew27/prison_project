import numpy as np 
import pandas as pd 

from cleaning_second_half import clean_all_second_half
from cleaning_first_half import clean_all_first_half




def load_all_years(save=False):
    """Loads all years and applies the below functions

    Args:
        save (bool, optional): If True saves as csv, otherwise returns DataFrame (DF). Defaults to False.

    Returns:
        DF: DataFrame w/ columns cleaned & created 
    """    
    df_1 = clean_all_first_half()
    df_1 = df_1[['term_clean', 'crime_clean', 'race_adjusted', 'nativity_no_states', 'Year']]
    df_1.columns =  ['term', 'crime', 'race', 'nativity', 'year']

    df_2 = clean_all_second_half()
    df_2 = df_2[['term_clean', 'crime_clean', 'race', 'clean_nationality', 'Year']]
    df_2.columns = ['term', 'crime', 'race', 'nativity', 'year']
    df_all = pd.concat([df_1, df_2])
    df_all['max_term'] = df_all['term'].apply(lambda x: max_apply(x))
    df_all['min_term'] = df_all['term'].apply(lambda x: x[0])
    df_all['avg_term'] = df_all['term'].apply(lambda x: avg_term(x))
    df_all['violent'] = df_all['crime'].apply(lambda x: violent_apply(x))
    df_all['violent_sexual'] = df_all['crime'].apply(lambda x: violent_sexual_apply(x))
    df_all['moral'] = df_all['crime'].apply(lambda x: moral_apply(x))
    df_all['property'] = df_all['crime'].apply(lambda x: property_apply(x))
    df_all['deceit'] = df_all['crime'].apply(lambda x: deceit_apply(x))
    df_all['uncategorized'] = df_all['crime'].apply(lambda x: uncategorized_apply(x))
    df_all['life_sentence'] = df_all['max_term'].apply(lambda x: life_sentence(x))
    df_all['death_sentence'] = df_all['max_term'].apply(lambda x: death_sentence(x))
    df_all['life_or_death_sentence'] = df_all['max_term'].apply(lambda x: life_or_death_sentence(x))
    df_all['nativity'] = df_all['nativity'].apply(lambda x: fix_nativity(x))
    df_all['foreign'] = df_all['nativity'].apply(lambda x: foreign(x))
    df_all['larceny'] = df_all['crime'].apply(lambda x: larceny(x))
    df_all['burglary'] = df_all['crime'].apply(lambda x: burglary(x))
    df_all['murder'] = df_all['crime'].apply(lambda x: murder(x))
    df_all['robbery'] = df_all['crime'].apply(lambda x: robbery(x))
    df_all['forgery'] = df_all['crime'].apply(lambda x: forgery(x))
    df_all['assault'] = df_all['crime'].apply(lambda x: assault(x))
    df_all['all_larceny'] = df_all['crime'].apply(lambda x: all_larceny(x))
    df_all['all_manslaughter'] = df_all['crime'].apply(lambda x: all_manslaughter(x))
    df_all['foreign_and_race_combined'] = df_all.apply(lambda row: nativity_race_combined(row), axis =1)
    df_all['nativity_race_with_countries'] = df_all.apply(lambda row: nativity_race_with_countries(row), axis =1)



    if save:
        df_all.to_csv('../../data/confined_data_final.csv')
    else:
        return df_all        


def nativity_race_with_countries(row):
    """Nativity if Nativity != US, otherwise Race

    Args:
        row (DF row): row of DF

    Returns:
        str: row's race or nativity depending on above
    """    
    if row['nativity'] != 'United States':
        return row['nativity']
    else:
        return row['race']

def nativity_race_combined(row):
    """Returns 'Foreign' if individual is foreign/white, otherwise returns race

    Args:
        row (DF row)

    Returns:
        [str]: [foreign or race]
    """    
    if row['race'] == 'White' and row['foreign'] == 1:
        return 'Foreign'

    return row['race']


def avg_term(x):
    """computes average term if possible - applicable when prisoner has prison term range, e.g. 4-6 years would be 5 

    Args:
        x (str/float): term listed

    Returns:
        float: average of sentence term
    """    
    if 'Life' in x or 'Death' in x or '?' in x:
        return None
    else:
        if len(x) == 2:
            return np.mean(x) 
        else:
            return x[0]
    
        



def all_manslaughter(x):
    """creates dummy column for manslaughter crimes

    Args:
        x (list): original crime(s)

    Returns:
        [int]: [1 if manslaughter, 0 if not]
    """    
    for elem in x:
        if elem == 'Manslaughter' or elem == 'Voluntary Manslaughter':
            return 1
        return 0 


def larceny(x):
    """creates dummy column for larceny crimes

    Args:
        x (list): original crime(s)

    Returns:
        [int]: [1 if larceny, 0 if not]
    """    
    for elem in x:
        if elem == 'Larceny':
            return 1
        return 0


def burglary(x):
    """creates dummy column for burglary crimes

    Args:
        x (list): original crime(s)

    Returns:
        [int]: [1 if burglary, 0 if not]
    """    
    for elem in x:
        if elem == 'Burglary':
            return 1
        return 0

def murder(x):
    """creates dummy column for murder crimes

    Args:
        x (list): original crime(s)

    Returns:
        [int]: [1 if murder, 0 if not]
    """    
    for elem in x:
        if elem == 'Murder':
            return 1
        return 0

def robbery(x):
    """creates dummy column for robbery crimes

    Args:
        x (list): original crime(s)

    Returns:
        [int]: [1 if robbery, 0 if not]
    """    
    for elem in x:
        if elem == 'Robbery':
            return 1
        return 0

def forgery(x):
    """creates dummy column for forgery crimes

    Args:
        x (list): original crime(s)

    Returns:
        [int]: [1 if forgery, 0 if not]
    """    
    for elem in x:
        if elem == 'Forgery':
            return 1
        return 0

def assault(x):
    """creates dummy column for assault crimes

    Args:
        x (list): original crime(s)

    Returns:
        [int]: [1 if assault, 0 if not]
    """    
    for elem in x:
        if 'Assault' in elem:
            return 1
        return 0 
def all_larceny(x):
    """creates dummy column for all_larceny (includes things like 'Grand Larceny' & 'Larceny as Bailee') crimes

    Args:
        x (list): original crime(s)

    Returns:
        [int]: [1 if all_larceny, 0 if not]
    """    
    for elem in x:
        if 'Larceny' in elem:
            return 1
        return 0 

def foreign(x): # electing to count 'Indian Territory' as domestic 
    """creates dummy column for foreign 

    Args:
        x (str): birthplace/ nativity

    Returns:
        [int]: [1 or 0]
    """
    if x == 'United States' or x == 'Indian Territory':
        return 0
    else:
        return 1


def fix_nativity(x):
    """Fixes nativity for years where nativity/race were combined

    Args:
        x (str): nativity

    Returns:
        str: original value or United States if value = 'Black'
    """    
    if x == 'Black':
        return 'United States'
    else:
        return x


def life_sentence(x):
    """Dummy column for life sentences

    Args:
        x (str/float): sentence

    Returns:
        int: 1 if sentence is 'Life' otherwise 0 
    """    
    if x == 'Life':
        return 1
    else:
        return 0

def death_sentence(x):
    """Dummy column for death sentences

    Args:
        x (str/float): sentence

    Returns:
        int: 1 if sentence is 'Death' otherwise 0 
    """    
    if x == 'Death':
        return 1
    else:
        return 0

def life_or_death_sentence(x):
    """Dummy column for death & life sentences

    Args:
        x (str/float): sentence

    Returns:
        int: 1 if sentence is 'Death' or 'Life' otherwise 0 
    """    
    if x == 'Life' or x == 'Death':
        return 1
    else:
        return 0


def violent_apply(x):
    """creates dummy column for violent crimes

    Args:
        x (list): original crime(s)

    Returns:
        [int]: [1 if violent, 0 if not]
    """    
    v_lst = ['Assault w/ Intent to Kill', 
             'Assault w/ Intent to Murder',
             'Assisting to Kill',
             'Assisting to Murder',
             'Attempted Murder',
             'Conspiring to Murder',
             'Murder',
             'Administering Poison', 
             'Assault',
             'Felonious Assault',
             'False Imp', # this is probably kidnapping 
             'Assault w/ Intent to Rob',
             'Manslaughter',
             'Voluntary Manslaughter',
             'Kidnapping',
             'Mayhem']
    for elem in x:
        if elem in v_lst:
            return 1
    return 0 

def violent_sexual_apply(x):
    """creates dummy column for violent/sexual crimes

    Args:
        x (list): original crime(s)

    Returns:
        [int]: [1 if violent/sexual, 0 if not]
    """    
    v_lst = ['Assault w/ Intent to Rape',
             'Assault to Ravish', # make sure this is spelled correctly 
             'Rape']
    for elem in x:
        if elem in v_lst:
            return 1
    return 0 

def moral_apply(x):
    """creates dummy column for moral crimes

    Args:
        x (list): original crime(s)

    Returns:
        [int]: [1 if moral, 0 if not]
    """    
    m_lst = ['Using Instruments with Intent to Commit Abortion',
             'Sodomy',
             'Abortion',
             'Bigamy',
             'Crime Against Nature',
             'Incest',
             'Buggary']
    for elem in x:
        if elem in m_lst:
            return 1
    return 0 


def property_apply(x):
    """creates dummy column for property crimes

    Args:
        x (list): original crime(s)

    Returns:
        [int]: [1 if property, 0 if not]
    """    
    p_lst = ['Arson',
             'Attempt to Rob',
             'Attempted Arson',
             'Attempted Robbery', 
             'Burglary', 
             'Defacing Brands',
             'Effacing and Defacing Brands',
             'Having Tools with Intent to Commit Burglary',
             'Having Tools with Intent to Enter Building',
             'Larceny',
             'Larceny as Bailee',
             'Larceny from Person',
             'Receiving Stolen Goods',
             'Stealing / Killing Cattle',
             'Stealing Stock',
             'Killing Cattle',
             'Killing Stock',
             'Robbery',
             'Having Burgular Tools',
             'Felony, Branding Stock',
             'Malicious Mischief',
             'Grand Larceny',
             'Obstructing of Railroad Track',
             'Train Wrecking',
             'Maliciously Destroying Check']
    for elem in x:
        if elem in p_lst:
            return 1
    return 0 

def deceit_apply(x): 
    """creates dummy column for deceit crimes

    Args:
        x (list): original crime(s)

    Returns:
        [int]: [1 if deceit, 0 if not]
    """    
    d_lst = ['Cheat',
            'Confidence Games',
            'Counterfeiting',
            'Embezzlement',
            'False Pretenses',
            'Forgery',
            'Having Ficticious Checks',
            'Illegal Voting',
            'Perjury',
            'Uttering',
            'Uttering Forgery']
    for elem in x:
        if elem in d_lst:
            return 1
    return 0 

def uncategorized_apply(x):
    """creates dummy column for uncategorized crimes

    Args:
        x (list): original crime(s)

    Returns:
        [int]: [1 if uncategorized, 0 if not]
    """    
    uncategorized_lst = ['Rescue of Prisoner',
                         'Conspiracy',
                         'Felony']
    for elem in x:
        if elem in uncategorized_lst:
            return 1
    return 0 


def max_apply(x):
    """Finds max sentence when sentence is a range

    Args:
        x (list): sentence

    Returns:
        float: [max sentence]
    """    
    if len(x) == 1:
        return x[0]
    else:
        return x[1]
        

# Below are - a method for averaging life sentences i did not use and a throwaway function 

# def avg_apply(x):
#     if len(x) == 1:
#         return x[0]
#     else:
#         if 'Life' in x:
#             return x[0] + (100 / 2)
#         else:
#             return (x[0] + x[1]) / 2

# def crime_counts():
#     df = load_all_years()
#     result = {}
#     for crimes in df['crime']:
#         for crime in crimes:
#             if crime in result:
#                 result[crime] += 1
#             else:
#                 result[crime] = 1
#     result = pd.Series(result)
#     result = result.sort_values(ascending=False)
#     return result 

if __name__=="__main__":
    df = load_all_years()
    load_all_years(True)
    # print(df.iloc[1410:1415])
    # print(df.info())
    # print(df.nativity_race_with_countries.value_counts())
    # load_all_years(True)
    # for yr in df.year.unique():
    #     yr_df = df[df.year == yr]
    #     print(yr)
    #     print(yr_df.race.value_counts())
    # df = df[df['nativity'] == 'Black']
    # print(df.race.unique())
    # print(df.nativity.unique())
    # print(df.info())
    # cc = list(crime_counts().index)
    # print(cc)
    # print(df.info())
    # print(df.iloc[:,0:10].tail())
    # print(df.iloc[:, 10:20].tail())
    # print(df.iloc[:, 20:].tail())
    # result = set()
    # for lst in df['term']:
    #     for term in lst:
    #         if isinstance(term, str):
    #             result.add(term)
    # print(result)
    # print(df['all_larceny'].value_counts())
    # df = load_all_years()
    # print(df.tail())
    # m_lst = ['Cheat',
    #         'Confidence Games',
    #         'Counterfeiting',
    #         'Embezzlement',
    #         'False Pretenses',
    #         'Forgery',
    #         'Having Ficticious Checks',
    #         'Illegal Voting',
    #         'Perjury',
    #         'Uttering',
    #         'Uttering Forgery']
    # for elem in m_lst:
    #     print(elem)
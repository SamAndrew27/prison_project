import numpy as np 
import pandas as pd 

from cleaning_second_half import clean_all_second_half
from cleaning_first_half import clean_all_first_half




def load_all_years(save=False):
    df_1 = clean_all_first_half()
    df_1 = df_1[['term_clean', 'crime_clean', 'race_adjusted', 'nativity_no_states', 'Year']]
    df_1.columns =  ['term', 'crime', 'race', 'nativity', 'year']

    df_2 = clean_all_second_half()
    df_2 = df_2[['term_clean', 'crime_clean', 'race', 'clean_nationality', 'Year']]
    df_2.columns = ['term', 'crime', 'race', 'nativity', 'year']
    df_all = pd.concat([df_1, df_2])
    df_all['max_term'] = df_all['term'].apply(lambda x: max_apply(x))
    df_all['min_term'] = df_all['term'].apply(lambda x: x[0])
    df_all['violent'] = df_all['crime'].apply(lambda x: violent_apply(x))
    df_all['violent_sexual'] = df_all['crime'].apply(lambda x: violent_sexual_apply(x))
    df_all['moral'] = df_all['crime'].apply(lambda x: moral_apply(x))
    df_all['property'] = df_all['crime'].apply(lambda x: property_apply(x))
    df_all['deceit'] = df_all['crime'].apply(lambda x: deceit_apply(x))
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


    if save:
        df_all.to_csv('../../data/all_data.csv')
    else:
        return df_all        


def larceny(x):
    for elem in x:
        if x == 'Larceny':
            return 1
        return 0


def burglary(x):
    for elem in x:
        if x == 'Burglary':
            return 1
        return 0

def murder(x):
    for elem in x:
        if x == 'Murder':
            return 1
        return 0

def robbery(x):
    for elem in x:
        if x == 'Robbery':
            return 1
        return 0

def forgery(x):
    for elem in x:
        if x == 'Forgery':
            return 1
        return 0

def assault(x):
    for elem in x:
        if 'Assault' in x:
            return 1
        return 0 
def all_larceny(x):
    for elem in x:
        if 'Larceny' in x:
            return 1
        return 0 

def foreign(x):
    if x == 'United States' or x == 'Indian Territory':
        return 1
    else:
        return 0


def fix_nativity(x):
    if x == 'Black':
        return 'United States'
    else:
        return x


def life_sentence(x):
    if x == 'Life':
        return 1
    else:
        return 0

def death_sentence(x):
    if x == 'Death':
        return 1
    else:
        return 0

def life_or_death_sentence(x):
    if x == 'Life' or x == 'Death':
        return 1
    else:
        return 0


def violent_apply(x):
    m_lst = ['Assault w/ Intent to Kill', 
             'Assault w/ Intent to Murder',
             'Assisting to Kill',
             'Assisting to Murder',
             'Attempted Murder',
             'Conspiring to Murder',
             'Murder',
             'Administering Poison', 
             'Assault',
             'Felonious Assault',
             'Assault w/ Intent to Rob',
             'Manslaughter',
             'Voluntary Manslaughter'
             'Kidnapping',
             'Mayhem']
    for elem in x:
        if elem in m_lst:
            return 1
    return 0 

def violent_sexual_apply(x):
    m_lst = ['Assault w/ Intent to Rape',
             'Assault to Ravish' # make sure this is spelled correctly 
             'Rape']
    for elem in x:
        if elem in m_lst:
            return 1
    return 0 

def moral_apply(x):
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
    m_lst = ['Arson',
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
             'Having Burgular Tools'
             'Felony, Branding Stock',
             'Malicious Mischief',
             'Grand Larceny',
             'Obstructing of Railroad Track',
             'Train Wrecking',
             'Maliciously Destroying Check']
    for elem in x:
        if elem in m_lst:
            return 1
    return 0 

def deceit_apply(x):
    m_lst = ['Cheat',
            'Confidence Games',
            'Conspiracy', # conspiracy can be for anything 
            'Counterfeiting',
            'Embezzlement',
            'False Imp', # this is probably kidnapping 
            'False Pretenses',
            'Forgery',
            'Having Ficticious Checks',
            'Illegal Voting',
            'Perjury',
            'Uttering',
            'Uttering Forgery']
    for elem in x:
        if elem in m_lst:
            return 1
    return 0 

def max_apply(x):
    if len(x) == 1:
        return x[0]
    else:
        return x[1]
        

def avg_apply(x):
    if len(x) == 1:
        return x[0]
    else:
        if 'Life' in x:
            return x[0] + (100 / 2)
        else:
            return (x[0] + x[1]) / 2





def death_life(save=False):
    df = load_all_years()
    life_df = df[df['max_term'] == 'Life']
    death_df = df[df['max_term'] == 'Death']
    both = pd.concat([life_df, death_df])
    if save:
        both.to_csv('../../data/life_death.csv')
    else:
        return both

def no_death_life(save=False):
    df = load_all_years()
    no_life_df = df[df['max_term'] != 'Life']
    no_death_df = df[df['max_term'] != 'Death']
    both = pd.concat([no_life_df, no_death_df])
    if save:
        both.to_csv('../../data/no_life_death.csv')
    else:
        return both

if __name__=="__main__":
    df = load_all_years()
    # df = df[df['nativity'] == 'Black']
    # print(df.race.unique())
    # print(df.nativity.unique())

    # ['United States' 'Canada' 'Italy' 'England' 'Ireland' 'Germany' 'France'
    # 'Austria' 'Mexico' 'Indian Territory' 'Prussia' 'Isle of Man' 'Saxony'
    # 'Nova Scotia' 'Bohemia' 'Russia' 'Scotland' 'Switzerland' 'Cuba'
    # 'Australia' 'Sweden' 'Norway' "Prince Edward's Island" 'Hungary' 'China'
    # 'Denmark' 'Alsace' 'Wales' 'Poland' 'On the Sea' 'East Indies' 'Black'
    # 'Mexican' '?' 'Swiss' 'Spanish' 'Japan']

    print(df.info()) 
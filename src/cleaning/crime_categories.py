import pandas as pd 

from join_years import load_all_years

def crime_lists():
    violent_crimes = [  'Assault w/ Intent to Kill', 
                        'Assault w/ Intent to Murder',
                        'Assisting to Kill',
                        'Assisting to Murder',
                        'Attempted Murder',
                        'Conspiring to Murder',
                        'Murder',
                        'Administering Poison', 
                        'Assault',
                        'Felonious Assault',
                        'False Imp', 
                        'Assault w/ Intent to Rob',
                        'Manslaughter',
                        'Voluntary Manslaughter',
                        'Kidnapping',
                        'Mayhem']

    violent_sexual_crimes = ['Assault w/ Intent to Rape',
                             'Assault to Ravish',
                             'Rape']

    moral_crimes = ['Using Instruments with Intent to Commit Abortion',
                    'Sodomy',
                    'Abortion',
                    'Bigamy',
                    'Crime Against Nature',
                    'Incest',
                    'Buggary']

    property_crimes = ['Arson',
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

    deceit_crimes = ['Cheat',
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
    uncategorized_lst = ['Rescue of Prisoner',
                         'Conspiracy',
                         'Felony']
    result = {'Deceit': deceit_crimes,
              'Moral': moral_crimes,
              'Property': property_crimes,
              'Violent': violent_crimes,
              'Violent Sexual': violent_sexual_crimes,
              'Uncategorized': uncategorized_lst}
    return result 

def crime_categories(save=False):
    df = load_all_years()
    crime_category_dic = crime_lists()
    idx_length = 0
    for cat, crime in crime_category_dic.items():
        idx_length += len(crime)
    
    crime_nativity_race = list(df['foreign_and_race_combined'].unique())

          
    result = pd.DataFrame(columns=['crime', 'category', 'race & nativity', 'number of incidents'], index=list(range(idx_length * len(crime_nativity_race))))


    crime_dic = {}


    for idx, row in df.iterrows():
        nat_race = row['foreign_and_race_combined']
        for crime in row['crime']:
            crime_nr = f'{crime}:{nat_race}'
            if crime_nr in crime_dic:
                crime_dic[crime_nr] += 1
            else:
                crime_dic[crime_nr] = 1
    
    idx = 0
    for category, crime_lst in crime_category_dic.items():
        for crime in crime_lst:
            for nr in crime_nativity_race:
                crime_nr = f'{crime}:{nr}'
                if crime_nr in crime_dic:
                    result.iloc[idx] = [crime, category, nr, crime_dic[crime_nr]]
                else:
                    result.iloc[idx] = [crime, category, nr,  0]
                idx += 1
    if save:
        result.to_csv('../../data/crime_categories.csv')
    else:
        return result 



if __name__=="__main__":
    # df = crime_categories()
    # print(df.head(50))
    # print(df.info())
    # crime_categories(True)
    # df = load_all_years()
    # print(df.info())
    # print(df.foreign_and_race_combined.unique())

    crime_categories(True)
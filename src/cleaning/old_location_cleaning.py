import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 


def load_location_data_and_clean(states = True, modernized=True, save=False):
    if states:
        df = pd.read_csv('../../data/original_data/state_data.csv')
        save_local = '../../data/state_data_cleaned_final.csv'
    else: 
        if modernized:
            df = pd.read_csv('../../data/original_data/foreign_data_modernized.csv')
            save_local = '../../data/foreign_data_modernized_cleaned_final.csv'

        else:
            df = pd.read_csv('../../data/original_data/foreign_data.csv')
            save_local = '../../data/foreign_data_cleaned_final.csv'



    df = df.rename(columns={'Unnamed: 0':'location'})
    year_df = df.iloc[:, 1:]
    yrs = list(year_df.columns)

    output_idx = list(range(len(yrs) * len(df['location'].unique())))
    result = pd.DataFrame(columns=['Location', 'Year', 'Prisoners'], index= output_idx) # stupid way to index and add, do something better 


    index = 0
    for idx, row in df.iterrows():
        location = row['location'].strip()
        for yr in yrs:
            total = row[yr]
            if total == None:
                total = 0
            result.iloc[index] = [location, yr, total]
            index += 1
    result = result.fillna(0)
    result['Prisoners'] = result['Prisoners'].astype(int)
    result['Year'] = result['Year'].astype(int)
    result['Region'] = result['Location'].apply(lambda x: regional_apply(x))

    if save:
        result.to_csv(save_local)
    else:
        return result



def regional_apply(x):
    if x in  [ 'Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island' , 'Vermont']:
        return 'New England (US)'
    elif x in ['Delaware', 'D.C.', 'Maryland', 'New Jersey', 'New York' , 'Pennsylvania']:
        return 'Mideast (US)'
    elif x in ['Illinois', 'Indiana', 'Michigan', 'Ohio', 'Wisconsin']:
        return 'Great Lakes (US)'
    elif x in ['Iowa', 'Kansas', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'South Dakota']:
        return 'Plains (US)'
    elif x in ['Alabama','Arkansas','Florida','Georgia','Kentucky','Louisiana','Mississippi', 'North Carolina', 'South Carolina', 'Tennessee', 'Virginia','West Virginia']:
        return 'Southeast (US)'
    elif x in ['Arizona', 'New Mexico', 'Oklahoma', 'Texas']:
        return 'Southwest (US)'
    elif x in ['Colorado', 'Idaho', 'Montana', 'Utah', 'Wyoming']:
        return 'Rocky Mountain (US)'
    elif x in ['California', 'Nevada', 'Oregon', 'Washington']:
        return 'Far West (US)'
    elif x in ['Alaska', 'Hawaii']:
        return 'Alaska & Hawaii'
    elif x in ['Brazil', 'Argentina']:
        return 'South America'
    elif x in ['Mexico', 'Nicaragua', 'Costa Rica']: # really mexico/central america --- combine with Caribbean? 
        return 'Central America'
    elif x in ['Jamaica', 'Cuba', 'Porto Rico']:
        return 'Caribbean'
    elif x in ['South Africa', 'Egypt', 'Turkey', 'Syria']:
        return 'Africa/Middle East'
    elif x in ['Australia', 'New Zealand', 'Solomon Islands']:
        return 'Oceania'
    elif x in ['Indonesia', 'Philippines', 'Thailand', 'India', 'China', 'South Korea', 'Japan']:
        return 'Asia'
    elif x in ['Portugal', 'Spain', 'Italy', 'Greece']:
        return 'Southern Europe'
    elif x in ['France', 'Ireland', 'United Kingdom', 'Germany', 'Austria', 'Netherlands', 'Switzerland', 'Belgium']:
        return 'Western Europe'
    elif x in ['Norway', 'Sweden', 'Finland', 'Lithuania', 'Denmark']:
        return 'Northern Europe'
    elif x in ['Poland','Czech Republic','Croatia', 'Serbia', 'Albania', 'Montenegro', 'Bulgaria', 'Romania', 'Hungary', 'Russia']:
        return 'Central & Eastern Europe'
    elif x == 'Canada':
        return x
    

    # Use the below link for European regions
    # https://en.wikipedia.org/wiki/Regions_of_Europe#/media/File:European_sub-regions_(according_to_EuroVoc,_the_thesaurus_of_the_EU).png



def regional_df(save=False): # do this again with foreign data as well once we see how they work in Tableau 
    states = load_location_data_and_clean()
    foreign = load_location_data_and_clean(False)
    df = pd.concat([states,foreign])
    regions = df['Region'].unique()
    years = df['Year'].unique()
    result_idx = list(range(len(years) * len(regions)))
    result = pd.DataFrame(columns=['Region', 'Year', 'Prisoners'], index=result_idx)

    idx = 0
    for region in regions:
        sub_df = df[df['Region'] == region]
        for year in years:
            year_df = sub_df[sub_df['Year'] == year]
            total = year_df['Prisoners'].sum()
            result.iloc[idx] = [region, year, total]
            idx += 1
    if save:
        result.to_csv('../../data/regional_data.csv')
    else:
        return result 


def state_sizes(years = [1878]):
    df = load_location_data_and_clean()
    yr1 = df[df.Year == years[0]] # probably better to just use an array of 0s and do no assignment or popping prior
    years.pop(0)
    result = pd.DataFrame(data=yr1['Prisoners'].values, index = list(df['Location'].unique()))
    # result = {}
    # states = list(df['State'].unique())

    for year in years:
        yr_df = df[df['Year'] == year]
        temp = pd.DataFrame(data=yr_df['Prisoners'].values, index = list(df['Location'].unique()))
        result = result + temp
    return result 


def state_sizes_multiple_ranges(year_ranges):
    # result = pd.DataFrame(columns = ['Year Range', 'State', 'Prisoners'])
    index = np.arange(0,51)
    for year_range in year_ranges:
        low = min(year_range)
        high = max(year_range)
        range_result = state_sizes(year_range)
        year_strings = [f'{low}-{high}'] * len(range_result.index)
        prisoner_totals = []
        for lst in range_result.values:
            for num in lst:
                prisoner_totals.append(num)
    
        if index[0] == 0:
            result = pd.DataFrame({'Year Range': year_strings, 'State': range_result.index, 'Prisoners':prisoner_totals}, index = index)
        else:
            result = pd.concat([result, pd.DataFrame({'Year Range': year_strings, 'State': range_result.index, 'Prisoners':prisoner_totals})])
        index += 49

    return result 


def create_grouped_df(groups=4, cutoff=500, cutoff_column = False,  save = False, filename = 'Default'):
    stop = groups
    df = load_location_data_and_clean()
    years = list(df['Year'].unique())
    iterations = int(len(years) / groups)
    indexes = np.arange(0, groups)
    start = 0
    years_lst = []
    for num in range(iterations):
        sub_year_lst = years[start:stop]
        years_lst.append(sub_year_lst)
        start += groups
        stop += groups
    result = state_sizes_multiple_ranges(years_lst)
    if cutoff_column:
        result['Prisoners w/ Cutoff'] =  result['Prisoners'].apply(lambda x: cutoff if x >= cutoff else x)
    else:
        result['Prisoners'] =  result['Prisoners'].apply(lambda x: cutoff if x >= cutoff else x) 
    if save:
        result.to_csv(f'../../data/{filename}.csv')
    else:
        return result 


            


if __name__=="__main__":
    # def load_location_data_and_clean(states = True, modernized=True, save=False):

    # load_location_data_and_clean(False, True, True)
    # load_location_data_and_clean(True, True, True)
    load_location_data_and_clean(False, False, True)



    # states = load_location_data_and_clean(False, True, False)
    # foreign = load_location_data_and_clean(True, True, False)

    # both = pd.concat([states,foreign])
    # print(both.info())

    # print(both.head())

    # na = both[pd.isnull(both['Region'])]
    # print(na.head())
    # print(na.Location.unique())
    # df = regional_df()
    # print(df.info())
    # print(df.head())
    # regional_df(True)
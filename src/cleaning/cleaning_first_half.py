
import pandas as pd 

def load_data_or_legend(data=True):
    if data:
        df = pd.read_csv('../../data/1878-1888_DATA.csv')
        return df
    else:
        legend = pd.read_csv('../../data/1878-1888_LEGEND.csv')
        return legend


def clean_term():
    df = load_data_or_legend()
    legend = load_data_or_legend(False)
    dic = {}
    tl = legend['Term Legend'].dropna()
    for elem in tl:
        temp = elem.split(':')
        dic[temp[0]] = temp[1].strip()
    df['term_clean'] = df['Term'].apply(lambda x: clean_term_apply(x, dic))
    return df
    
    
def clean_term_apply(x, dic):
    x = x.strip()
    if x in dic:
        x = dic[x]
        return [x]
    else:
        if '-' in x:
            x = x.split('-')
            for elem in x:
                elem = float(elem.strip())
            return x 
        else:
            if x == '?':
                return None 
            else:
                return [float(x)]


def clean_crime():
    df = load_data_or_legend()
    legend = load_data_or_legend(False)
    dic = {}
    for elem in legend['Crime Legend'].dropna():
        elem = elem.split(':')
        dic[elem[0]] = elem[1].strip()
    df['crime_clean'] = df['Crime'].apply(lambda x: clean_crime_apply(x, dic))
    return df
    
def clean_crime_apply(x,dic):
    x = x.split('&')
    result = []
    for elem in x:
        s_elem = elem.strip()
        if s_elem in dic:
            result.append(dic[s_elem])
        else:
            result.append(s_elem)

    return result


if __name__=="__main__":
    df= clean_crime()
    vc = df.crime_clean.value_counts()
    vc = list(vc.index)
    print(vc)
    # print(clean_crime())
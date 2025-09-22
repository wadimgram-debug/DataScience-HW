# data_preprocessing
import pandas as pd

def preproc_cnt_null(data):  
    cols_with_na = data.columns[data.isnull().any()]

    if len(cols_with_na) == 0:
         print("Пропусков нет")
    else:
         for col in cols_with_na:
           print(f"{col}: {data[col].isnull().sum()} пропусков")

def preproc_cnt_duplicates(data):
    total_duplicates = data.duplicated().sum()
    print(f"Количество полностью совпадающих строк: {total_duplicates}")

def preproc_fill(data):
    df = data.copy()
    #удалим "лишние" столбцы 
    df.drop(['Unnamed: 0'],axis=1,inplace=True)
    df.drop(['Date','Day'],axis=1,inplace=True)
    print("Столбцы Unnamed, Date, Day удалены")
    #есть символы, убираем
    df['Precipitation'] = df['Precipitation'].str.split(' ').str[0]
    #что нельзя преобразовать в число - удаляем
    df['Precipitation'] = pd.to_numeric(df['Precipitation'], errors='coerce')
    print("Столбец Precipitation преобразован")

    for col in df.columns:
        if df[col].isnull().any():
           df[col].fillna(df[col].mean(), inplace=True)
    print("Пропуски заполнены")

    return df
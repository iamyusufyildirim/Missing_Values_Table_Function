###################################
# Eksik Değerler (Missing Values) #
###################################
# Gözlemlerde eksiklik olmasını durumunu ifade etmektedir.


# İlgili kütüphane importları ve bazı görsel ayarlamaları yapıyoruz.
import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.float_format", lambda x : "%.3f" % x)

# İlgili veri setini projemize dahil ediyoruz.
df = sns.load_dataset("titanic")


# Veri setindeki eksik değer bilgisini miktar ve oran olacak bir formatta
# görme isteğimizi na_table adında fonksiyon ile Python'a ifade ediyoruz.
def missing_values_table(dataframe, na_name=False):
    na_columns = [col for col in dataframe.columns if dataframe[col].isnull().sum() > 0]
    na_values = (dataframe[na_columns].isnull().sum()).sort_values(ascending=False)
    ratio = (dataframe[na_columns].isnull().sum() / dataframe.shape[0] * 100).sort_values(ascending=False)
    table = pd.concat([na_values, ratio], axis=1, keys=["Value", "%"])
    print(table)

    if na_name:
        print(na_columns)

missing_values_table(dataframe=df)..
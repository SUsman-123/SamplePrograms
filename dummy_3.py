'''
#File import
import pandas as pd
df = pd.read_csv("pokemon_data.csv")
print(df)
'''

# 1 Problem
import pandas as pd
df = pd.read_csv("pokemon_data.csv")
col = df.index[0:800:1]
print(col)
''''
if col % 2 == 0:
    df['Sum'] = df['Attack'] + df['Defense'] + df['Speed']
    print(df)'''

'''
#2 problem
def swap_columns(df, col1, col2):
    col_list = list(df.columns)
    x, y = col_list.index(col1),col_list.index(col2)
    col_list[y],col_list[x] = col_list[x], col_list[y]
    df = df[col_list]
    return df
df = swap_columns(df, 'Type 1','Type 2')
print(df)

col_list = list(df)
col_list[2],col_list[3] = col_list[3],col_list[2]
df.columns = col_list
print(df)
'''
#df.loc[:,['Name','Type 2','Type 1','HP','Attack','Sp. Atk','Sp. Def','Speed','Generation','Legendary']]
#print(df)
'''
#3rd problem
import pandas as pd
df=pd.read_csv("pokemon_data.csv")
df=df.loc[df["Name"].str.startswith('B', na=False)]
print(df)
'''

'''
#4 problem
import pandas as pd
df=pd.read_csv("pokemon_data.csv")
df["#"] = pd.date_range("20130101", periods=800)
df.set_index("#",inplace=True)
print(df)
'''
'''
#5 Problem
import pandas as pd
df=pd.read_csv("pokemon_data.csv")
print((df.head(5)["Defense"]).sum())
print((df.tail(5)["Defense"]).sum())

print((df.groupby(["Defense","HP"]).sum()))
'''


















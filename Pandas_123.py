'''
import pandas as pd
s = pd.Series([3,-5,7,4], index=['a','b','c','d'])
print(s)'''

import pandas as pd

data = {'Country':['India','england','United states'],
        'Capital':['Delhi','London','Brizel'],
        'Country Code':['+91','+66','+34']
}
#df = pd.DataFrame(data)
df = pd.DataFrame(data,columns=['Country','Country Code','Capital'])
print(df)









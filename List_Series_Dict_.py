# Creating a list
'''
import pandas as pd
list_1 = ['hello','i am ','usamn']
se = pd.Series(list_1)
print(type(se))
print(se)'''
'''import pandas as pd
list_1 = ['Average','Good','Excellent']
list_2 = [5,7,9]
l1 = pd.Series(list_1)
l2 = pd.Series(list_2)
frame = {'Author':l1,'Xerox':l2}
result = pd.DataFrame(frame)
#print(result)
#Adding one column
marks = [60,70,90]
result['Marks'] = pd.DataFrame(marks)
print(result)'''

'''import pandas as pd
d= {'Cat':'cute','Dog':'furr'}
print(dx)
print(d['Cat'])
print(d.get('horse','N/A'))
del d['Cat']
print(d.get('Cat','N/A'))'''
import pandas as pd
dx = {'person':2,'spyder':8,'cat':4}
for animal in dx:
    legs = dx[animal]````````````````
    print("A %s has %d legs ",(animal,legs))


























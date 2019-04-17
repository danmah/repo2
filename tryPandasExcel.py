import pandas as pd

'''
#  print(dir(pd))

xls = pd.ExcelFile('dada.xlsx')

for sn in xls.sheet_names:
    print(sn)

dataf = xls.parse(xls.sheet_names[0])

print(dataf.head())

# for row in dataf.lines:
#     for cell in row:
#         print(cell)

sh1 = xls.parse(0)

# b = sh1.axes
# print(b)

'''

dataf = pd.read_excel('dada.xlsx', sheet_name='Feuil1')

#  MesNoms = dataf['Nom']  # Ceci fonctionne

#  dataf.iloc[[1, 3, 5], [1, 3]]
#  dataf.iloc[1:5, 2:4]
#  dataf.iloc[1, 1]

print(dataf.iloc[2, 0])
print(dataf.loc[2, 'ShortID'])

sh = dataf.shape

for i in range(sh[0]):  # rows
    for j in range(sh[1]):  # columns
        print(dataf.iloc[i, j], end='\t')
    print()


#  Ça fonctionne plus bas!
'''
l1 = dataf.values.tolist()
print('Valeurs en liste de listes')
print(l1)

l2 = dataf.values.flatten()
print('Valeurs à la queue leu leu (une liste)')
print(l2)

# dataframe.to_dict will make the keys 0, 1, 2 being the keys
l3 = dataf.to_dict()
print('Simple to_dict()')
print(l3)

l4 = dataf.set_index('ShortID').T.to_dict('list')
print()
print(l4)
'''

'''
These steps can be done with the following line:

>>> df.set_index('ID').T.to_dict('list')
{'p': [1, 3, 2], 'q': [4, 3, 2], 'r': [4, 0, 9]}
In case a different dictionary format is needed, here are examples of the possible orient arguments. Consider the following simple DataFrame:

>>> df = pd.DataFrame({'a': ['red', 'yellow', 'blue'], 'b': [0.5, 0.25, 0.125]})
>>> df
        a      b
0     red  0.500
1  yellow  0.250
2    blue  0.125
Then the options are as follows.

dict - the default: column names are keys, values are dictionaries of index:data pairs

>>> df.to_dict('dict')
{'a': {0: 'red', 1: 'yellow', 2: 'blue'},
 'b': {0: 0.5, 1: 0.25, 2: 0.125}}
list - keys are column names, values are lists of column data

>>> df.to_dict('list')
{'a': ['red', 'yellow', 'blue'],
 'b': [0.5, 0.25, 0.125]}
series - like 'list', but values are Series

>>> df.to_dict('series')
{'a': 0       red
      1    yellow
      2      blue
      Name: a, dtype: object,

 'b': 0    0.500
      1    0.250
      2    0.125
      Name: b, dtype: float64}
split - splits columns/data/index as keys with values being column names, data values by row and index labels respectively

>>> df.to_dict('split')
{'columns': ['a', 'b'],
 'data': [['red', 0.5], ['yellow', 0.25], ['blue', 0.125]],
 'index': [0, 1, 2]}
records - each row becomes a dictionary where key is column name and value is the data in the cell

>>> df.to_dict('records')
[{'a': 'red', 'b': 0.5},
 {'a': 'yellow', 'b': 0.25},
 {'a': 'blue', 'b': 0.125}]
index - like 'records', but a dictionary of dictionaries with keys as index labels (rather than a list)

>>> df.to_dict('index')
{0: {'a': 'red', 'b': 0.5},
 1: {'a': 'yellow', 'b': 0.25},
 2: {'a': 'blue', 'b': 0.125}}


======================================

Suppose your dataframe is as follows:

>>> df
   A  B  D ID
0  1  3  2  p
1  4  3  2  q
2  4  0  9  r
1. Use set_index to set ID columns as the dataframe index.

    df.set_index("ID", drop=True, inplace=True)
2. Use the orient=index parameter to have the index as dictionary keys.

    dictionary = df.to_dict(orient="index")
The results will be as follows:

    >>> dictionary
    {'q': {'A': 4, 'B': 3, 'D': 2}, 'p': {'A': 1, 'B': 3, 'D': 2}, 'r': {'A': 4, 'B': 0, 'D': 9}}

 '''


'''
sh1 = xls.sheet_name(0)
sh2 = xls.sheet_name(1)

for i in range(10):
    print(sh1.col(i)(i))
print('allo')

>>> xl = pd.ExcelFile("dummydata.xlsx")
>>> xl.sheet_names
[u'Sheet1', u'Sheet2', u'Sheet3']
>>> df = xl.parse("Sheet1")
>>> df.head()

'''

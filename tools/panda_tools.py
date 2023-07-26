import numpy as np
import pandas as pd
import csv_tools
import sys

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
types = ['Rent', 'Utilities', 'Internet']


rent = np.array(['2023-01-01', '2023-01-01', '2023-01-01', '2021-10-06', '2023-02-01', '2023-02-01', '2023-03-10', '2023-03-10', '2023-03-10', '2023-03-10', '2023-03-10', '2023-03-10'])
utilities = np.array(['2023-01-01', '2023-01-01', '2023-01-01', '2021-10-06', '2023-02-01', '2023-02-01', '2023-03-10', '2023-03-10', '2023-03-10', '2023-03-10', '2023-03-10', '2023-03-10'])
internet = np.array(['2023-01-01', '2023-01-01', '2023-01-01', '2021-10-06', None, '2023-02-01', '2023-03-10', '2023-03-10', '2023-03-10', '2023-03-10', '2023-03-10', '2023-03-10'])
d = np.array([pd.to_datetime(rent), pd.to_datetime(utilities), pd.to_datetime(internet)])

df = pd.DataFrame(data=d, columns=months, index=types)
#print(df)

dataPath = sys.path[0] + '/../data/lau2023.csv'
df2 = csv_tools.read_csv(dataPath)
print(df2)
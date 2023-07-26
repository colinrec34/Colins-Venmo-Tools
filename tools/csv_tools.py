import pandas as pd

#Reading formatted year csv into data frame
names = ['Ben', 'Colin', 'Fineas', 'JJ', 'Lucas', 'Noah', 'Quinn', 'Man']
def read_year_file(dataPath):
    with open(dataPath) as file:
        data = {}
        lines = file.readlines()
        for name in names:
            n = names.index(name)
            dates = []
            for i in range(1, 13):
                dates.append(lines[13*n+i].replace('\n', '').split(','))
            data[name] = dates
        return pd.DataFrame(data)
#-------------------------------------------------------------
if __name__=='__main__':
    import sys
    dataPath = sys.path[0] + '/../data/2023.csv'
    df = read_year_file(dataPath)
    print(df)
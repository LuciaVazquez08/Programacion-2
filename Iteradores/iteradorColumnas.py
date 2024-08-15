import pandas as pd 
class ColumIterator:
    def __init__(self,dataframe):
        self.df = dataframe
        self.columns = list(dataframe.columns)
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.columns):
            column = self.df[self.columns[self.index]]
            self.index += 1
            return column
        else:
            raise StopIteration

df = pd.DataFrame({'A': [1,2,3], "B": [4,5,6]})
print('test')

col_iter = ColumIterator(df)
for col in col_iter:
    print(col)
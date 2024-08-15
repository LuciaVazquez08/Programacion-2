import pandas as pd 

class RowIterator:
    def __init__(self,dataframe):
        self.df = dataframe
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.df):
            row = self.df.iloc[self.index]
            self.index += 1
            return row
        else:
            raise StopIteration
    
    def hasnext(self):
        if self.index < len(self.df) - 1:
            return True
        else:
            return False


df = pd.DataFrame({'A': [1,2,3], "B": [4,5,6]})
print('test')
row_iter = RowIterator(df)
for row in row_iter:
    print(row)
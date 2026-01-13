# This is a sample pipeline script that takes a month as a command-line argument

import sys
import pandas as pd

print("argurment", sys.argv)

month = int(sys.argv[1]) 

# Sample DataFrame creation
df = pd.DataFrame({
    'day': [1, 2, 3],
    'Psg': ['a', 'b', 'c']
})
df['month'] = month
print(df.head())

df.to_parquet(f'output_{month}.parquet', index=False)

print(f'hello pipeline, month={month}')


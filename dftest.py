from numpy import dtype
import pandas as pd

df =pd.DataFrame(columns=['code','name','unit_price'])
# df.set_index('code')
print(df)
temp_df = pd.read_csv('master.csv', encoding='utf-8',header=0, dtype={'code':str,'name':str,'unit_price':int})
print('****** temp_df ******')
print(temp_df)
master_df = pd.concat([df,temp_df],keys='code')
master_df.set_index('code')

print('****** master_df ******')
print(master_df)
print(master_df.loc['2','price'])
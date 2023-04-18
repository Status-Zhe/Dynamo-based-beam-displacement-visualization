import pandas as pd
data = pd.read_excel('DynamicStrain.xlsx', sheet_name='Sheet1')
print(data.shape[0])
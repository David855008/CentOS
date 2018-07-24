import pandas as pd
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45],
				   'Time': [15, 25, 35, 45, 55, 65, 75]})
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='David')
writer.save()
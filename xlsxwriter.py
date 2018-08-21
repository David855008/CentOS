import pandas as pd
import xlsxwriter
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45],
				   'Time': [15, 25, 35, 45, 55, 65, 75]})
writer = pd.ExcelWriter('testing.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='David')
writer.save()

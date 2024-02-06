import pandas as pd
df_ssl = pd.read_csv("docs\quests\DDA\SpineSurgeryList.csv")
meters =  df_ssl['신장'] * 0.01
df_ssl['키'] = meters
df_meters = df_ssl['키']
df_weight = df_ssl['체중']
BMIs = df_weight / (df_meters**2)
df_ssl['BMI'] = BMIs
df_ssl['BMI'] = df_ssl['BMI'].round(2)
print(df_ssl['BMI'])
df_ssl['수술시간'].info()
pass
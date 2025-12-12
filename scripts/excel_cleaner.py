# excel_cleaner.py
import pandas as pd

df = pd.read_excel("input.xlsx")
df = df.dropna().drop_duplicates()
df.to_excel("cleaned.xlsx", index=False)

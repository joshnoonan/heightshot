import pandas as pd

a = pd.read_csv("1718.csv")
b = pd.read_csv("1819.csv")
b = b.dropna(axis=1)
merged = a.merge(b)
merged.to_csv("warriors.csv", index=False)



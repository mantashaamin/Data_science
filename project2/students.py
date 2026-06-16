import pandas as pd
import os

print("Current directory:", os.getcwd())
print("Script file:", __file__)

script_dir = os.path.dirname(os.path.abspath(__file__))
print("Script directory:", script_dir)

csv_path = os.path.join(script_dir, "students.csv")
print("CSV path:", csv_path)

df = pd.read_csv(csv_path)

print(df)
print(df.head(3))
print(df.tail(3))
df[df["math"] > 80]["name"]
(df["math"] > 80) & (df["physics"] > 80)
df[(df["math"] > 80) & (df["chemistry"] > 90)]["name"]
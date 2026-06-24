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

# filtering
math_above_80 = df[df["math"] > 80]["name"]

# multiple conditions
math_and_physics_above_80 = df[(df["math"] > 80) & (df["physics"] > 80)]

math_above_80_chem_above_90 = df[
    (df["math"] > 80) & (df["chemistry"] > 90)
]["name"]

# aggregation
lowest_chemistry_student = df[
    df["chemistry"] == df["chemistry"].min()
]["name"]

# count filtered rows
chemistry_below_80_count = df[df["chemistry"] < 80].shape[0]

# create total column
df["total"] = df["math"] + df["physics"] + df["chemistry"]

# total marks series
total_marks = df["total"]

# highest total
highest_total = df["total"].max()

# topper row
topper_row = df[df["total"] == highest_total]

# topper name
topper_name = topper_row["name"]

# topper using idxmax
topper_using_idxmax = df.loc[df["total"].idxmax()]

# sorted by total (highest first)
sorted_by_total = df.sort_values("total", ascending=False)

# name frequencies
name_counts = df["name"].value_counts()

# unique names
unique_name_count = df["name"].nunique()

# dataset summary
summary_stats = df.describe()

#groupby() = split data into groups, then perform an operation on each group.
group = df.groupby("class")["total"].mean() # gives avg
group_max=df.groupby("class")["total"].max()# max
group_min=df.groupby("class")["total"].min()#lowest 
group_count=df.groupby("class")["name"].count()#count number of student 

print("Topper:")
print(topper_name)

print("\nHighest Total:")
print(highest_total)

print("\nName Counts:")
print(name_counts)

print("\nUnique Names:")
print(unique_name_count)

print("\nSummary Statistics:")
print(summary_stats)

print("\navg total per class:")
print(group)

print("\n highest score: ")
print(group_max)

print("\n lowest score")
print(group_min)

print("\n count number of student")
print(group_count)
print("-----------------------------------------------------------")
x = df.groupby("class").agg({
    "math": ["mean", "max"],
    "physics": ["mean", "min"],
    "chemistry": ["mean", "max"]
})
print(x)
print("--------------------------------------------------------------")
def get_grade(total):
    if total >= 270:
        return "A"
    elif total >= 240:
        return "B"
    else:
        return "C"

df["grade"] = df["total"].apply(get_grade)

print(df)
print("--------------------------------------------------------------")
import matplotlib.pyplot as plt
grade_counts = df["grade"].value_counts()

plt.bar(
    grade_counts.index,
    grade_counts.values
)

plt.show()
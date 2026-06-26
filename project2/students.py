import pandas as pd
import os
# ============================================================
# PANDAS NOTES
# ============================================================
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
import matplotlib.pyplot as plt

# ============================================================
# MATPLOTLIB NOTES 
# ============================================================

# plot()      -> Show trends or compare values over an ordered axis
# bar()       -> Compare categories
# hist()      -> Show distribution of a numerical column
# scatter()   -> Show relationship between two numerical columns
# pie()       -> Show percentage / part of a whole
#
# Useful Parameters:
# title()     -> Adds graph title
# xlabel()    -> X-axis label
# ylabel()    -> Y-axis label
# grid()      -> Adds grid lines
# legend()    -> Shows labels of multiple plots
# figure()    -> Changes figure size
# marker=      -> Changes point style
# linestyle=   -> Changes line style
# linewidth=   -> Changes line thickness
# bins=        -> Number of ranges in histogram
# color=       -> Changes graph color
# autopct=     -> Shows percentages in pie chart
# savefig()    -> Saves graph as image
# subplot()    -> Multiple graphs in one figure


# ============================================================
# 1. BAR CHART
# Question:
# How many students received each grade?
#
# Why bar chart?
# Grades are categories (A, B, C).
# We compare counts.
# ============================================================

grade_counts = df["grade"].value_counts()

plt.figure(figsize=(6,4))

plt.bar(
    grade_counts.index,
    grade_counts.values,
    color="skyblue"
)
# Save graph
plt.savefig("barchat.png")
plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.grid(axis="y")

plt.show()


# ============================================================
# 2. HISTOGRAM
# Question:
# How are total marks distributed?
#
# Why histogram?
# Total marks are numerical values.
# Histogram groups them into ranges (bins).
# ============================================================

plt.figure(figsize=(8,5))

plt.hist(
    df["total"],
    bins=5,
    color="orange"
)
# Save graph
plt.savefig("mark_distribution.png")
plt.title("Distribution of Total Marks")
plt.xlabel("Total Marks")
plt.ylabel("Number of Students")
plt.grid()

plt.show()


# ============================================================
# 3. SCATTER PLOT
# Question:
# Is there any relationship between Math and Physics marks?
#
# Why scatter?
# Both columns are numerical.
# Scatter helps identify positive/negative relationships.
# ============================================================

plt.figure(figsize=(6,5))

plt.scatter(
    df["math"],
    df["physics"]
)
# Save graph
plt.savefig("scatter.png")
plt.title("Math vs Physics")
plt.xlabel("Math Marks")
plt.ylabel("Physics Marks")
plt.grid()

plt.show()


# ============================================================
# 4. LINE PLOT + LEGEND
# Question:
# Compare Math and Physics marks of students.
#
# Why line plot?
# Helps compare two subjects student by student.
# ============================================================

plt.figure(figsize=(8,5))

plt.plot(
    df["name"],
    df["math"],
    marker="o",
    label="Math"
)

plt.plot(
    df["name"],
    df["physics"],
    marker="o",
    label="Physics"
)
# Save graph
plt.savefig("marks_distribution.png")
plt.title("Math vs Physics Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.grid()

plt.legend()

plt.show()


# ============================================================
# 5. SUBPLOTS
# Display multiple graphs inside one figure.
# ============================================================

plt.figure(figsize=(10,8))

# First graph

plt.subplot(2,1,1)

plt.bar(
    df["name"],
    df["math"],
    color="lightgreen"
)
# Save graph

plt.title("Math Marks")

# Second graph

plt.subplot(2,1,2)

plt.plot(
    df["name"],
    df["physics"],
    marker="o",
    linestyle="--",
    linewidth=3,
    label="Physics"
)

plt.title("Physics Marks")
plt.legend()

plt.tight_layout()

# Save graph
plt.savefig("student_report.png")

plt.show()


# ============================================================
# MINI EDA PROJECT
# ============================================================

# ------------------------------------------------------------
# Q1. Find the highest scoring student.
#
# Pandas
#
# Why?
# Only one student is required.
#
# Functions:
# idxmax()
# loc[]
# ------------------------------------------------------------

top_student = df.loc[df["total"].idxmax()]

print("Highest Scoring Student")
print(top_student)

# Insight:
# Returns the complete row of the student having
# the highest total marks.



# ------------------------------------------------------------
# Q2. Which class performs the best on average?
#
# Pandas:
# groupby()
# mean()
#
# Visualization:
# Bar Chart
# ------------------------------------------------------------

class_avg = df.groupby("class")["total"].mean()

print(class_avg)

plt.figure(figsize=(6,4))

plt.bar(
    class_avg.index,
    class_avg.values,
    color="green"
)
# Save graph
plt.savefig("avg.png")
plt.title("Average Total Marks By Class")
plt.xlabel("Class")
plt.ylabel("Average Marks")
plt.grid(axis="y")

plt.show()

# Insight:
# Class having the tallest bar has the highest average marks.



# ------------------------------------------------------------
# Q3. How are grades distributed?
#
# Pandas:
# value_counts()
#
# Visualization:
# Bar Chart
# Pie Chart (if percentages are required)
# ------------------------------------------------------------

grade_counts = df["grade"].value_counts()

print(grade_counts)

# ---------- BAR CHART ----------

plt.figure(figsize=(6,4))

plt.bar(
    grade_counts.index,
    grade_counts.values,
    color="skyblue"
)
# Save graph
plt.savefig("grade.png")
plt.title("Grade Distribution")
plt.xlabel("Grades")
plt.ylabel("Number of Students")

plt.grid(axis="y")

plt.show()


# ---------- PIE CHART ----------

plt.figure(figsize=(6,6))

plt.pie(
    grade_counts.values,
    labels=grade_counts.index,
    autopct="%1.1f%%"
)
# Save graph
plt.savefig("pie.png")
plt.title("Grade Distribution")

plt.show()

# Insight:
# Shows how grades are distributed among students.



# ------------------------------------------------------------
# Q4. How are total marks distributed?
#
# Visualization:
# Histogram
#
# Why?
# Total marks are numerical values.
# Histogram groups them into ranges using bins.
# ------------------------------------------------------------

plt.figure(figsize=(8,5))

plt.hist(
    df["total"],
    bins=5,
    color="orange"
)
# Save graph
plt.savefig("marks.png")
plt.title("Distribution of Total Marks")
plt.xlabel("Total Marks")
plt.ylabel("Number of Students")

plt.grid()

plt.show()

# Insight:
# Helps identify where most students scored.



# ------------------------------------------------------------
# Q5. Is there any relationship between Math and Physics?
#
# Visualization:
# Scatter Plot
# ------------------------------------------------------------

plt.figure(figsize=(6,5))

plt.scatter(
    df["math"],
    df["physics"]
)

plt.title("Math vs Physics")
plt.xlabel("Math Marks")
plt.ylabel("Physics Marks")

plt.grid()

plt.show()

# Insight:
# If dots move upward from left to right,
# there is a positive relationship.



# ------------------------------------------------------------
# Q6. Compare Math and Physics marks.
#
# Visualization:
# Line Plot + Legend
# ------------------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    df["name"],
    df["math"],
    marker="o",
    label="Math"
)

plt.plot(
    df["name"],
    df["physics"],
    marker="o",
    label="Physics"
)
# Save graph
plt.savefig("line.png")
plt.title("Math vs Physics Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.grid()

plt.legend()

plt.show()

# Insight:
# Compares both subjects student-wise.

# ============================================================
# INTERVIEW THINKING PROCESS
# ============================================================

# Question
#        ↓
# Numerical or Categorical?
#
#        ↓
# One value?
# -> max(), min(), mean(), sum()
#
#        ↓
# Group comparison?
# -> groupby()
#
#        ↓
# Count categories?
# -> value_counts()
#
#        ↓
# Need Visualization?
#
# Compare Categories
# -> Bar Chart
#
# Distribution
# -> Histogram
#
# Relationship
# -> Scatter Plot
#
# Trend
# -> Line Plot
#
# Percentage
# -> Pie Chart
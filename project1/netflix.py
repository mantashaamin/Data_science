import numpy as np
import pandas as pd

print("-- STEP 1: Creating the Raw Netflix Data Matrix --")
# 0 represents unwatched movies
raw_matrix = np.array([
    [5, 4, 0, 1],  # User A
    [0, 2, 4, 0],  # User B
    [3, 0, 0, 5]   # User C
])
print("Original NumPy Array:\n", raw_matrix)

print("\n--- STEP 2: Moving to Pandas & Replacing 0 with NaN ---")
# Replace 0 with NaN because 0 isn't a real rating; it's missing data
raw_matrix_with_nan = np.where(raw_matrix == 0, np.nan, raw_matrix)

df = pd.DataFrame(
    raw_matrix_with_nan, 
    index=['User A', 'User B', 'User C'], 
    columns=['Sci-Fi', 'Comedy', 'Drama', 'Action']
)
print("Pandas DataFrame with Missing Values:\n", df)

print("\n--- STEP 3: Cleaning Data (Imputation) ---")
# Fill missing watched movies with a neutral rating of 3.0
df_cleaned = df.fillna(3.0)
print("Cleaned Data:\n", df_cleaned)

print("\n--- STEP 4: Feature Aggregation (Averages) ---")
genre_averages = df_cleaned.mean(axis=0)
user_averages = df_cleaned.mean(axis=1)
print("Average Rating per Genre:\n", genre_averages)
print("\nAverage Rating per User:\n", user_averages)

print("\n--- STEP 5: Data Filtering (Targeted Marketing) ---")
action_lovers = df_cleaned[df_cleaned['Action'] >= 4.0]
print("Users who love Action movies (>= 4.0 stars):\n", action_lovers)
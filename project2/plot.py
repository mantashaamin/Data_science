import matplotlib.pyplot as plt
'''
students = ["Priya", "Rahul", "Amit"]

marks = [100, 200, 300]

plt.plot(students, marks)

plt.show()

plt.bar(
    ["A", "B", "C"],
    [10, 30, 20],
    color="pink"
)

plt.title("Student Marks")

plt.xlabel("Students")

plt.ylabel("Marks")
plt.grid()

plt.show()
'''
grade_counts = df["grade"].value_counts()

plt.bar(
    grade_counts.index,
    grade_counts.values
)

plt.show()
'''
plt.bar(
    class_avg.index,
    class_avg.values
)

plt.title("Average Marks By Class")

plt.show()
'''
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
print(tips.head())
'''"countplot() counts how many observations fall into each category.
barplot() summarizes a numerical variable for each category, using the mean by default.'''
sns.countplot(
    data=tips,
    x="day"
)

plt.show()
'''So what does hue do?

It colors the points based on a category.

It does not change the x-axis.

It does not change the y-axis.'''
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="day"
)
plt.savefig("hue.png")
plt.show()

'''
Smoker -> Different marker shape
style="sex"
style="day"
style="smoker"
style="time"
'''

tips = sns.load_dataset("tips")

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex",
    style="smoker"
)

plt.title("Total Bill vs Tip")
plt.savefig("smoker")
plt.show()

'''| total_bill |  tip | sex    | smoker | day  | time   | size |
| ---------- | ---: | ------ | ------ | ---- | ------ | ---- |
| 16.99      | 1.01 | Female | No     | Sun  | Dinner | 2    |
| 10.34      | 1.66 | Male   | No     | Sun  | Dinner | 3    |
| 21.01      | 3.50 | Male   | No     | Sun  | Dinner | 3    |
| 24.59      | 3.61 | Female | No     | Sat  | Dinner | 4    |
| 15.20      | 2.00 | Male   | Yes    | Thur | Lunch  | 2    |
'''
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="day",
    style="time"
)
plt.savefig("scatterplot.png")
plt.show()
'''| Parameter | Controls            | Example          |
| --------- | ------------------- | ---------------- |
| `x`       | Horizontal position | `x="total_bill"` |
| `y`       | Vertical position   | `y="tip"`        |
| `hue`     | Color               | `hue="sex"`      |
| `style`   | Marker shape        | `style="day"`    |
'''
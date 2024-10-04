"""
Aryan Mitharwal
A3 - CS 2410
"""

import seaborn as sns
import matplotlib.pyplot as plt

# DATASET
tips = sns.load_dataset("tips")

# 1. Bar Chart: Average total bill per day
plt.figure()
bar_chart = tips.groupby('day')['total_bill'].mean().plot(kind='bar', title='Average Total Bill Per Day')
plt.ylabel('Average Total Bill ($)')
plt.tight_layout()
plt.show()

# 2. Line Chart: Total bill trends over time (using index as time for simplicity)
plt.figure()
line_chart = tips['total_bill'].plot(kind='line', title='Total Bill Trend Over Time', xlabel='Order Index', ylabel='Total Bill ($)')
plt.tight_layout()
plt.show()

# 3. Pie Chart: Distribution of bills by day
plt.figure()
pie_data = tips.groupby('day')['total_bill'].sum()
pie_chart = pie_data.plot(kind='pie', autopct='%1.1f%%', title='Distribution of Total Bills by Day')
plt.ylabel('')
plt.tight_layout()
plt.show()

# 4. Scatter Plot: Tip vs. Total Bill
plt.figure()
scatter_chart = tips.plot(kind='scatter', x='total_bill', y='tip', title='Tip vs. Total Bill')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.tight_layout()
plt.show()

# 5. Histogram: Distribution of total bill amounts
plt.figure()
hist_chart = tips['total_bill'].plot(kind='hist', bins=10, title='Distribution of Total Bill Amounts')
plt.xlabel('Total Bill ($)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

"""
Explanations of Graphs!

Bar Chart: The bar chart shows that Saturday has the highest average total bill compared to other days, while Thursday tends to have the lowest average total bill.
Line Chart: The line chart demonstrates fluctuations in total bills, with no clear upward or downward trend, indicating the variability in order size.
Pie Chart: The pie chart reveals that Saturday and Sunday together account for the majority of total bills, with Thursday and Friday contributing less.
Scatter Plot: The scatter plot shows a positive correlation between the total bill amount and the tip amount, meaning that higher bills generally result in higher tips.
Histogram: The histogram of total bills indicates that most bills fall between $10 and $20, with fewer high-cost meals.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load employee data
df = pd.read_csv("employees.csv")

print("Employee Data:")
print(df.head())
# Bar Chart

avg_salary = df.groupby("department")["salary"].mean()

bars = plt.bar(avg_salary.index, avg_salary.values)
plt.bar_label(bars)

plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.savefig("bar_chart.png")
plt.show()

# Histogram

plt.figure()

plt.hist(df["salary"], bins=5)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.savefig("histogram.png")
plt.show()
# Scatter Plot

plt.figure()

for dept in df["department"].unique():
    dept_data = df[df["department"] == dept]

    plt.scatter(
        dept_data["id"],
        dept_data["salary"],
        label=dept
    )

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()

plt.savefig("scatter_plot.png")
plt.show()

# Line Chart

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

plt.figure()

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("line_chart.png")
plt.show()

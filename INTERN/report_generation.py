import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt

#Step 1: Read CSV file
data = pd.read_csv("employee_data.csv")

# Step 2: Analysis
total_employees = len(data)
average_salary = data['Salary'].mean()
department_counts = data['Department'].value_counts()

# Step 3: Create chart
department_counts.plot(kind='bar', color='green')
plt.title("Employees per Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("chart.png")
plt.close()

# Step 4: Create PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Employee Report", ln=True, align="C")

pdf.set_font("Arial", size=12)
pdf.ln(10)
pdf.cell(200, 10, txt=f"Total Employees: {total_employees}", ln=True)
pdf.cell(200, 10, txt=f"Average Salary: Rs.{average_salary:.2f}", ln=True)

pdf.ln(10)
pdf.cell(200, 10, txt="Employees per Department:", ln=True)
for dept, count in department_counts.items():
    pdf.cell(200, 10, txt=f"{dept}: {count}", ln=True)

# Step 5: Add chart
pdf.image("chart.png", x=10, y=100, w=100)

# Step 6: Save report
pdf.output("employee_report.pdf")
print("✅ PDF report generated as employee_report.pdf")


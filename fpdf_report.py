import csv
from fpdf import FPDF

# ---------- Read CSV Data ----------
employees = []
salaries = []

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        employees.append(row)
        salaries.append(int(row["Salary"]))

# ---------- Data Analysis ----------
total_employees = len(employees)
average_salary = sum(salaries) / total_employees
highest_salary = max(salaries)
lowest_salary = min(salaries)

# ---------- Create PDF ----------
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Employee Salary Report", ln=True, align="C")
pdf.ln(5)

# Summary
pdf.set_font("Arial", "", 12)
pdf.cell(0, 8, f"Total Employees: {total_employees}", ln=True)
pdf.cell(0, 8, f"Average Salary: Rs. {average_salary:.2f}", ln=True)
pdf.cell(0, 8, f"Highest Salary: Rs. {highest_salary}", ln=True)
pdf.cell(0, 8, f"Lowest Salary: Rs. {lowest_salary}", ln=True)

pdf.ln(6)

# Table Header
pdf.set_font("Arial", "B", 11)
pdf.cell(30, 10, "Emp ID", border=1)
pdf.cell(40, 10, "Name", border=1)
pdf.cell(40, 10, "Department", border=1)
pdf.cell(30, 10, "Salary", border=1, ln=True)

# Table Rows
pdf.set_font("Arial", "", 11)
for emp in employees:
    pdf.cell(30, 10, emp["Employee_ID"], border=1)
    pdf.cell(40, 10, emp["Name"], border=1)
    pdf.cell(40, 10, emp["Department"], border=1)
    pdf.cell(30, 10, emp["Salary"], border=1, ln=True)

# Save PDF
pdf.output("Employee_Salary_Report.pdf")

print("Employee Salary PDF Report Generated Successfully!")

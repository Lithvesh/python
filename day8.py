import random
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def generate_data(num_students):
    data = []
    for i in range(1, num_students + 1):
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)
        performance_index = (marks * 0.6 + assignment * 0.4) * math.log(attendance + 1)
        student = (i, marks, attendance, assignment, performance_index)
        data.append(student)
    return data
def classify_students(data):
    categories = {
        "At Risk": [],
        "Average": [],
        "Good": [],
        "Top Performer": []
    }
    for student in data:
        sid, marks, attendance, assignment, _ = student
        if marks < 40 or attendance < 50:
            categories["At Risk"].append(sid)
        elif 40 <= marks <= 70:
            categories["Average"].append(sid)
        elif 71 <= marks <= 90:
            categories["Good"].append(sid)
        elif marks > 90 and attendance > 80:
            categories["Top Performer"].append(sid)
    return categories
def analyze_data(df):
    marks_array = df['Marks'].values
    mean_marks = sum(marks_array) / len(marks_array)
    median_marks = np.median(marks_array)
    std_dev = np.std(marks_array)
    summary_tuple = (mean_marks, std_dev, max(marks_array))
    correlation = df['Marks'].corr(df['Attendance'])
    min_val = min(marks_array)
    max_val = max(marks_array)
    df['Normalized Marks'] = [(x - min_val) / (max_val - min_val) for x in marks_array]
    return mean_marks, median_marks, std_dev, summary_tuple, correlation
def system_insight(df, categories):
    std_dev = np.std(df['Marks'])
    attendance_risk = len([x for x in df['Attendance'] if x < 50])
    top_performers = len(categories["Top Performer"])
    if std_dev < 15 and top_performers >= 2:
        return "Stable Academic System"
    elif attendance_risk > 3:
        return "Critical Attention Required"
    else:
        return "Moderate Performance"
roll_number = 23
num_students = roll_number % 10
if num_students < 10:
    num_students = 10
data = generate_data(num_students)
df = pd.DataFrame(data, columns=[
    "Student_ID", "Marks", "Attendance", "Assignment", "Performance_Index"
])
categories = classify_students(data)
mean_marks, median_marks, std_dev, summary_tuple, correlation = analyze_data(df)
final_result = system_insight(df, categories)
print("\n--- Student Data ---")
print(df)
print("\n--- Categories ---")
print(categories)
print("\n--- Statistical Summary ---")
print(f"Mean: {mean_marks}")
print(f"Median: {median_marks}")
print(f"Standard Deviation: {std_dev}")
print(f"Correlation (Marks vs Attendance): {correlation}")
print("\n--- Tuple Output ---")
print(summary_tuple)
print("\n--- Final Insight ---")
print(final_result)
plt.hist(df['Marks'])
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
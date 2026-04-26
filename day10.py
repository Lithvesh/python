import random
import math
import numpy as np
import pandas as pd
import copy
def generate_students(n=12):
    students = []
    for i in range(n):
        student = {
            "id": i + 1,
            "marks": random.randint(40, 100),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 30), random.randint(10, 30)]
        }
        students.append(student)
    return students
def mutate_data(data, roll_no):
    indices_to_modify = []
    rule = roll_no % 3
    for i in range(len(data)):
        if i % (rule + 1) == 0:
            indices_to_modify.append(i)
    for i in indices_to_modify:
        data[i]["marks"] = data[i]["marks"] + math.sqrt(data[i]["marks"])
        data[i]["scores"][0] += 5
        data[i]["scores"][1] += 3
        data[i]["attendance"] += 2
    return data
def manual_mean(marks_list):
    total = sum(marks_list)
    return total / len(marks_list)
def analyze(original, modified):
    orig_marks = np.array([s["marks"] for s in original])
    mod_marks = np.array([s["marks"] for s in modified])
    mean_orig = np.mean(orig_marks)
    mean_mod = np.mean(mod_marks)
    median = np.median(mod_marks)
    std_dev = np.std(mod_marks)
    manual = manual_mean(mod_marks)
    drift = abs(mean_orig - mean_mod)
    normalized = (mod_marks - np.min(mod_marks)) / (np.max(mod_marks) - np.min(mod_marks))
    return mean_mod, median, std_dev, drift, normalized, manual
def classify(drift, original, shallow):
    threshold = 5
    if original != original_backup:
        return "Copy Failure Detected"
    if drift < 2:
        return "Stable Data"
    elif drift < threshold:
        return "Minor Drift"
    else:
        return "Critical Drift"
roll_no = 526
original_data = generate_students()
original_backup = copy.deepcopy(original_data)
shallow_copy = copy.copy(original_data)
deep_copy = copy.deepcopy(original_data)
mutate_data(shallow_copy, roll_no)
mutate_data(deep_copy, roll_no)
df_original = pd.DataFrame(original_data)
df_shallow = pd.DataFrame(shallow_copy)
df_deep = pd.DataFrame(deep_copy)
mean_mod, median, std_dev, drift, normalized, manual = analyze(original_data, deep_copy)
result = classify(drift, original_data, shallow_copy)
print("\nOriginal DataFrame:\n", df_original)
print("\nShallow Copy DataFrame:\n", df_shallow)
print("\nDeep Copy DataFrame:\n", df_deep)
print("\nDrift Value:", drift)
print("Manual Mean:", manual)
print("\nTuple Output:", (mean_mod, drift, std_dev))
print("\nFinal Classification:", result)
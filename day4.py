q=int(input("Enter number of scores:"))
scores = []
for i in range(q):
    x = int(input("Enter score:"))
    scores.append(x)
D = 110011526
low_risk = []
medium_risk = []
high_risk = []
critical_risk = []
ignored_count = 0
valid_count = 0
removed_count = 0

for score in scores:
    if score < 0:
        ignored_count += 1
    else:
        valid_count += 1
        if score >= 0 and score <= 30:
            low_risk.append(score)
        elif score >= 31 and score <= 60:
            medium_risk.append(score)
        elif score >= 61 and score <= 100:
            high_risk.append(score)
        else:
            critical_risk.append(score)
print(f"Register Digit (D): {D}")
print(f"Initial Low Risk: {low_risk}")
print(f"Initial Medium Risk: {medium_risk}")
print(f"Initial High Risk: {high_risk}")
print(f"Initial Critical Risk: {critical_risk}")

if D % 2 == 0:
    print("Logic: D is EVEN. Removing all Low Risk entries.")
    for item in low_risk:
        removed_count += 1
    low_risk = []
else:
    print("Logic: D is ODD. Removing all Critical Risk entries.")
    for item in critical_risk:
        removed_count += 1
    critical_risk = []

print("After Personalized Filtering:")
print(f"Low Risk: {low_risk}")
print(f"Medium Risk: {medium_risk}")
print(f"High Risk: {high_risk}")
print(f"Critical Risk: {critical_risk}")
print(f"Total Valid Entries: {valid_count}")
print(f"Ignored Entries: {ignored_count}")
print(f"Removed Due to Personalization: {removed_count}")
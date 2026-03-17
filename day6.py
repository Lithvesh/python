n = int(input("Enter number of users: "))
for user in range(1, n + 1):
    print(f"\n--- User {user} ---")
    tr = list(map(int, input("Enter transactions (space-separated): ").split()))
    ca = {
        "normal": [],
        "large": [],
        "high_risk": [],
        "invalid": []
    }
    for t in tr:
        if t <= 0:
            ca["invalid"].append(t)
        elif 1 <= t <= 500:
            ca["normal"].append(t)
        elif 501 <= t <= 2000:
            ca["large"].append(t)
        else:
            ca["high_risk"].append(t)
    valid_tr = [t for t in tr if t > 0]
    num_tr = len(tr)
    total_value = sum(valid_tr)
    high_risk_count = len(ca["high_risk"])
    frequent = num_tr > 5
    large_spending = total_value > 5000
    sus = high_risk_count >= 3
    repeat_flag = False
    count = 1
    for i in range(1, len(tr)):
        if tr[i] == tr[i - 1]:
            count += 1
            if count > 2:
                repeat_flag = True
                break
        else:
            count = 1
    if repeat_flag:
        final_risk = "High Risk"
    elif sus or (frequent and large_spending):
        final_risk = "High Risk"
    elif frequent or large_spending:
        final_risk = "Moderate Risk"
    else:
        final_risk = "Low Risk"
    print("\nCategorized Transactions:")
    for key, value in ca.items():
        print(f"{key}: {value}")
    print("\nTotal Transaction Value:", total_value)
    print("Number of Transactions:", num_tr)
    print("\nPattern Detection:")
    print("Frequent Transactions:", frequent)
    print("Large Spending:", large_spending)
    print("Suspicious Pattern:", sus)
    print("Repeated Transactions (>2 times):", repeat_flag)
    print("\nFinal Risk Classification:", final_risk)
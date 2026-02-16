x=int(input("enter number of requests:"))
requests= []
for i in range(x):
    v=int(input("enter value for request:"))
    requests.append(v)
full_name= "Lithvesh Aditya Mothukuri"
L = 0
for ch in full_name:
    if ch != " ":
        L = L + 1
PLI = L % 3
no_demand = []
low_demand = []
moderate_demand = []
high_demand = []
invalid_requests = []
total_valid = 0
for req in requests:
    if req < 0:
        invalid_requests.append(req)

    elif req == 0:
        no_demand.append(req)
        total_valid = total_valid + 1
    elif req >= 1 and req <= 20:
        low_demand.append(req)
        total_valid = total_valid + 1
    elif req >= 21 and req <= 50:
        moderate_demand.append(req)
        total_valid = total_valid + 1
    else:
        high_demand.append(req)
        total_valid = total_valid + 1
removed_count = 0
if PLI == 0:
    removed_count = len(low_demand)
    low_demand = []
elif PLI == 1:
    removed_count = len(high_demand)
    high_demand = []
else:
    removed_count = len(low_demand) + len(high_demand)
    low_demand = []
    high_demand = []
print("Full Name Length (L):", L)
print("PLI Value:", PLI)
print("Total Valid Requests:", total_valid)
print("Removed Requests due to PLI:", removed_count)
print("No Demand:", no_demand)
print("Low Demand:", low_demand)
print("Moderate Demand:", moderate_demand)
print("High Demand:", high_demand)
print("Invalid Requests:", invalid_requests)
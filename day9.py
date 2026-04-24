import copy
def create_inventory():
    return [
        {
            "item": "Laptop",
            "details": {"price": 50000, "stock": 10, "supplier": {"rating": 4.5}}
        },
        {
            "item": "Phone",
            "details": {"price": 20000, "stock": 25, "supplier": {"rating": 4.2}}
        }
    ]
def apply_discount(data, roll_number):
    index_to_modify = roll_number % len(data)
    for i in range(len(data)):
        data[i]["details"]["price"] *= 0.9
        if i == index_to_modify:
            data[i]["details"]["stock"] -= 5
            data[i]["details"]["supplier"]["rating"] += 0.1
def compare_data(original, modified):
    changed = 0
    unchanged = 0
    for i in range(len(original)):
        if original[i] == modified[i]:
            unchanged += 1
        else:
            changed += 1
    return (changed, unchanged)
def main():
    roll_number = 526
    original_inventory = create_inventory()
    shallow_copy_inventory = original_inventory.copy()
    deep_copy_inventory = copy.deepcopy(original_inventory)
    apply_discount(shallow_copy_inventory, roll_number)
    apply_discount(deep_copy_inventory, roll_number)
    shallow_result = compare_data(original_inventory, shallow_copy_inventory)
    deep_result = compare_data(original_inventory, deep_copy_inventory)
    print("\n--- ORIGINAL INVENTORY ---")
    for item in original_inventory:
        print(item)
    print("\n--- SHALLOW COPY INVENTORY ---")
    for item in shallow_copy_inventory:
        print(item)
    print("\n--- DEEP COPY INVENTORY ---")
    for item in deep_copy_inventory:
        print(item)
    print("\n--- ANALYSIS ---")
    print("Shallow Copy Comparison:", shallow_result)
    print("Deep Copy Comparison:", deep_result)
main()
n = int(input("Enter number of students: "))
marks = []
for i in range(n):
    m = int(input("Enter mark: "))
    marks.append(m)
valid_count = 0
fail_count = 0
print("\nResults:")
for mark in marks:
    if mark < 0 or mark > 100:
        print(str(mark) + " → Invalid")
    else:
        valid_count += 1
        final_mark = mark
        if mark % 7 == 0:
            final_mark = mark + 10
            if final_mark > 100:
                final_mark = 100
        if final_mark >= 90:
            print(str(mark) + " → Excellent")
        elif final_mark >= 75:
            print(str(mark) + " → Very Good")
        elif final_mark >= 60:
            print(str(mark) + " → Good")
        elif final_mark >= 40:
            print(str(mark) + " → Average")
        else:
            print(str(mark) + " → Fail")
            fail_count += 1
print("Total Valid Students:", valid_count)
print("Total Failed Students:", fail_count)

student_id = input("Enter Student ID: ")
email = input("Enter Email: ")
password = input("Enter Password: ")
referral = input("Enter Referral Code: ")

sid_valid = (len(student_id) == 6 and
             student_id[:3] == "CSE" and
             student_id[3] == "-" and
             student_id[4].isdigit() and
             student_id[5].isdigit() and
             student_id[6].isdigit())

email_valid = False
if "@" in email and "." in email:
    at_pos = email.find("@")
    if 0 < at_pos < len(email) - 1 and email.endswith(".edu"):
        email_valid = True

pass_valid = False
if len(password) >= 8 and password[0].isupper():
    if any(char.isdigit() for char in password):
        pass_valid = True

ref_valid = (len(referral) == 6 and
             referral[:3] == "REF" and
             referral[3].isdigit() and
             referral[4].isdigit() and
             referral[5] == "@")

if sid_valid and email_valid and pass_valid and ref_valid:
    print("APPROVED")
else:
    print("REJECTED")
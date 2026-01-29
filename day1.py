age=int(input("Enter Age:"))
full_name=input("Enter Full Name:")
email=input("Enter Email ID:")
mobile=input("Enter Mobile Number:")
valid=True
if full_name[0]==" " or full_name[-1]==" ":
    valid=False
elif full_name.count(" ")<1:
    valid=False
if email.count("@")<1 or email.count(".")<1:
    valid=False
elif email[0]=="@":
    valid=False
if len(mobile)!=10:
    valid=False
elif not mobile.isdigit():
    valid=False
elif mobile[0]=="0":
    valid=False
if age<18 or age>60:
    valid=False
if valid:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")
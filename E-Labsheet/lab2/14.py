n1 = str(input("Username: "))
n2 = str(input("Password: "))

if ADMIN_USERNAME == n1 :
    if ADMIN_PASSWORD == n2 :
        print("Welcome, admin.")
    else:
        print("You are not admin.")
else:
    print("You are not admin.")
print("---<< Main Menu >>---")
print("    <B>urger Meal")
print("    <C>hicken Meal")
print("    <P>asta Meal")
total = 0
c1 = str(input("Enter your choice: "))
if c1 == "B" :
    print("---<< Burger Sub Menu >>---")
    print("    <R>egular Burger")
    print("    <C>heese Burger")
    print("    <D>ouble Cheese Burger")
    c2 = str(input("Enter your choice: "))
    if c2 == "R" :
        print("Your Regular Burger is 60 Baht.")
    elif c2 == "C" :
        print("Your Cheese Burger is 75 Baht.")
    else :
        print("Your Double Cheese Burger is 90 Baht.")
elif c1 == "C" :
    print("---<< Chicken Sub Menu >>---")
    print("    <F>ried Chicken")
    print("    <G>rilled Chicken")
    print("    <C>hef's Chicken")
    c2 = str(input("Enter your choice: "))
    if c2 == "F" :
        print("Your Fried Chicken is 120 Baht.")
    elif c2 == "G" :
        print("Your Grilled Chicken is 150 Baht.")
    else :
        print("Your Chef's Chicken is 180 Baht.")
elif c1 == "P" :
    print("---<< Pasta Sub Menu >>---")
    print("    <S>paghetti de Italiano")
    print("    <L>asagna Supreme")
    print("    <M>acaroni Special")
    c2 = str(input("Enter your choice: "))
    if c2 == "S" :
        print("Your Spaghetti is 90 Baht.")
    elif c2 == "L" :
        print("Your Lasagna Supreme is 120 Baht.")
    else :
        print("Your Macaroni Special is 100 Baht.")

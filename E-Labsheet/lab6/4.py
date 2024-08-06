count  , point = 1 , 0
while True :
    print(f"Frame # {count}")
    down = int(input("  Number of pins down: "))
    point += down
    if down < 10 :
        print(f"Frame # {count}")
        down = int(input(f"  Number of pins down (0-{10-down}): "))
        point += down
    count += 1
    if count == 11:
        break
print(f"Total score is {point}")

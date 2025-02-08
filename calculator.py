exit = False

def calc(needed, level, base_level):
    if needed == 0:
        return 0
    if level == base_level:
        return needed
    else:
        a = needed//2
        r = needed%2
        t = a*5+r*3
        print(f"{a}*5 + {r}*3 = {t} of level {level-1}")
        return calc(t, level-1, base_level)
    

print("Merge Calculator")
print()

while not exit:
    li = input("What level is your required item? ")
    try:
        l = int(li)
    except:
        print("Error: Please enter an integer!")
        print()
        continue
    
    ni = input("How many do you need? ")
    try:
        n = int(ni)
    except:
        print("Error: Please enter an integer!")
        print()
        continue
    
    bli = input("What level are you building with? ")
    try:
        bl = int(bli)
    except:
        print("Error: Please enter an integer!")
        print()
        continue
    
    print()

    if n<1 or l<1 or bl<1:
        print("Error: Item levels/quantity must be at least 1!")
        print()
        continue
    if bl > l:
        print("Error: Base level cannot be higher than desired level!")
        print()
        continue

    print(f"You need {calc(n, l, bl)} of level {bl}.")
    print()
    
    restart = str(input("Enter y to restart; otherwise press any key. "))
    print()
    if restart != "y":
        exit = True

# Error catching:
# input type checking
# non-zero, non-negative inputs
# base level must be less than level

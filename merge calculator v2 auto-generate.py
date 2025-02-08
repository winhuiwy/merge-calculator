def calculate(level, num):
    if (level==1):
        return num
    else:
        if (num%2==0):
            return calculate(level-1, 5*num/2)
        else:
            return calculate(level-1, 3 + 5*(num-1)/2)

# Prints what is needed for 1 or 2 items of level 1 to 9 at one go.
# Assumption: we are building using level 1s only.
print("Welcome to Winnie's merge calculator! ")
exit = False

while (not exit):
    print("Level:     1: 2:")
    for i in range(1,9):
        n1 = int(calculate(i, 1))
        n2 = int(calculate(i, 2))
        print("Level ", i, ": ", n1, " ", n2)
        

    cont = input("Type 'y' to restart. ")
    if (cont=="y" or cont=="Y"):
        print()
        continue
    else:
        exit = True

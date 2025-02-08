def calculate(level, num):
    if (level==1):
        return num
    else:
        if (num%2==0):
            return calculate(level-1, 5*num/2)
        else:
            return calculate(level-1, 3 + 5*(num-1)/2)

print("Welcome to Winnie's merge calculator! ")
exit = False

while (not exit):
    l = input("Enter level you want: ")
    n = input("How many? ")
    b = input("Forming using what level? ")

    try:
        li = int(l)
        ni = int(n)
        bi = int(b)

    except:
        print("Please enter integers.")


    print("You need ", int(calculate(li-bi+1, ni)), " level ", bi, "s.")

    cont = input("Type 'y' to restart. ")
    if (cont=="y" or cont=="Y"):
        print()
        continue
    else:
        exit = True

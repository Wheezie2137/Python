salary=int(input("Enter your salary:"))
if salary>=1000:
    print("A")
    if salary>=2000:
        print("C")
        if salary>=3000:
            print("H")
        print("M")
    else:
        print("D")
        if salary>=1500:
            print("J")
        else:
            print("I")
        print("L")
    print("N")
else:
    print("B")
    if salary>=500:
        print("E")
    else:
        print("F")
    print("K")
print("O")
print("P")

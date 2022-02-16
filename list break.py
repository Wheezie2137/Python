nums=[]
print("Enter 0 to end")
while True:
    no=int(input("Enter any number"))
    if no==0:
        break
    nums.append(no)

print("You have entered",len(nums),"values")
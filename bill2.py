bill=int(input("Enter your bill:"))
paid=int(input("Enter paid amount:"))
balance=paid-bill
print("Balance:",balance)

if balance >=50:
    fifty=int(balance/50)
    print("number of £50 notes to use:",fifty)
    balance=balance-(fifty*50)

if balance >=20:
    twenty=int(balance/20)
    print("number of £20 notes to use:",twenty)
    balance=balance-(twenty*20)

if balance >=10:
    print("number of £10 notes to use:",1)
    balance=balance-10

if balance >=5:
    print("number of £5 notes to use:",5)
    balance=balance-5

if balance >=2:
    two=int(balance/2)
    print("number of £2 coins to use:",two)
    balance=balance-(two*2)

if balance >=1:
    print("number of £1 coins to use:",1)
   




# Author Tow 11/9/2020

unique_1 = input("Please give a unique word")
unique_2 = input("Please give another unique word")
uq_3 = input(' Please give one more unique word')

uq_1 = unique_1.lower()
uq_2 = unique_2.lower()
uq_3 = uq_3.lower()

if uq_1 < uq_2 < uq_3:
    print("The words go in this order-")
    print(unique_1, unique_2, uq_3)
elif uq_1 < uq_3 < uq_2:
    print("The words go in this order-")
    print(unique_1, uq_3, unique_2)
elif uq_2 < uq_1 < uq_3:
    print("The words go in this order-")
    print(unique_2, unique_1, uq_3)
elif uq_2 < uq_3 < uq_1:
    print("The words go in this order-")
    print(unique_2, uq_3, unique_1)
elif uq_3 < uq_2 < uq_1:
    print("The words go in this order-")
    print(uq_3, unique_2, unique_1)
else:
    print("The words go in this order-")
    print(uq_3, unique_1, unique_2)

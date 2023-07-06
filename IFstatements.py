# is_hot=False
# is_cold=True

# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of Water!")
# # print("enjoy your day!")
# elif is_cold:
#     print("It's a cold day!")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day!")
# print("enjoy your day!")
# Exercise problem
credit=input("What is your credit value?")
credite=int(credit)
if credite>=10000:
    print("good credit")
    downpay=0.1*credite
    print("10% down payment")
else:
    print("Bad credit")
    downpay=0.2*credite
    print("20% down payment")
print(f"Down Payment: ${downpay}")

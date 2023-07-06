customer={
    "name":"Tushar",
    "age":21,
    "is_verified":True
}
customer["gender"]="male"
print(customer["name"])
# print(customer["Age"]) returns an error
# a more efficient way would be using the get method which returns
# a none value if not present
print(customer.get("Age"))
# we can also add a value using the get in the dictonary
print(customer.get("Birthdate","1st April 2002"))
print(customer["gender"])
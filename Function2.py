def greet_user(firstname, lastname):
    print(f'Hi {firstname} {lastname}!')
    print('Welcome aboard!')


print('Start!')
greet_user("Smith","John")#postional arguments, as
# the position defines the value the parameter gets
greet_user(lastname="Smith", firstname="Hon")#Keyword arguments,
# we don't have to worry about the order of the parameters
# improves readibility
print("finish!")
# always use a positional argument first and then 
# use a keyword argument, otherwise it'll give an error

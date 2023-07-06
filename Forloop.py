# for loop variable in String:
# for item in 'Tushar':
#     print(item)
# for item in ['Mosh','Tushar','Apoorva']:
#     print(item)
# for item in [1,2,3,4]:
#     print(item)
# for item in range(10): -> creates and object that we can iterate over,in each iteration this object spits out a new number 
#     print(item)
# for item in range(5,10): -> in this we give the atarting index in the range function too
#     print(item)
# for item in range(5,10,2): -> in this we include a step size in the range function therefore it iterates over the step size
#     print(item)
sum=0
for i in [10,20,30]:
    sum=sum+i 
print(f"total:{sum}")

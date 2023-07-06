# names=['tushar','Pearl','bhavya','garv']
# print(names)
# print(names[2])
# print(names[1])
# print(names[-2])
# print(names[2:])
# print(names[:3])
# print(names[1:3])
# names[0]='tusar'
# print(names)

# OUTPUTS:
# ['tushar', 'Pearl', 'bhavya', 'garv']
# bhavya
# Pearl
# bhavya
# ['bhavya', 'garv']
# ['tushar', 'Pearl', 'bhavya']
# ['Pearl', 'bhavya']
# ['tusar', 'Pearl', 'bhavya', 'garv']
num=[1,2,3,90,345,23,676,4,99]
max=num[0]
for i in num:
    if i>max:
        max=i
    # else:
    #     max=num[j]
print(max)
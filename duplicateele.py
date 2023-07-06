nums=[2,2,3,4,5,5,7]
uni=[]
for i in nums:
    if i not in uni:
        uni.append(i)
print(uni)
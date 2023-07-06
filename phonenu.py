phone = input("Enter your phone number: ")
Number={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}
output=""
for i in phone:
    # print(Number[i])
    output+=Number.get(i,"!")+ " "
print(output)
i=0
ans=7
while i<3:
    guess=int(input(f"Guess {i+1}: "))
    if ans==guess:
        print("yay you won!")
        break 
    i=i+1
if ans!=guess:
    print("Try again!")
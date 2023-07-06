weight=int(input('Weight: '))
KorL=input('(L)bs or (K)g: ')
if KorL=='L' or KorL=='l':
    kgs=0.45*weight
    print(f"Your weight in (K)gs is: {kgs}")
elif KorL=='K' or KorL=='k':
    lbs=weight/0.45
    print(f"Your weight in (L)bs is : {lbs}")
else:
    print("Entered the wrong choice")

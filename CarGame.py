command=""
counts=0
countp=0
while True : # command!="quit":
    command=input("> ").lower()
    # command=input(">")
    if command=="help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif command=="start" : # and count==0:
        if counts==0:
            print("Car started...")
            counts=counts+1
        else:
            print("Car has already been started!")
    elif command=="stop":
        if countp==0:
            print("Car stopped")
            countp=countp+1
        else:
            print("Car has already been stopped!")
    elif command=="quit":
        break
    else:
        print("I didn't undertand this...")
if command=="quit":
    print("Exit-ed")


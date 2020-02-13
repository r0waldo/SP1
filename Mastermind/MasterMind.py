def menu():
    print("************MASTERMIND**************")

    choice = input("""
    A: GameMaster
    B: Gokker
    Q: Stoppen

    Please enter your choice: """)

    if choice == "A" or choice =="a":
        gamemaster()
    elif choice == "B" or choice =="b":
        gokker()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A,B or Q.")
        print("Please try again")
menu()

def gokker():

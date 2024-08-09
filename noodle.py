name = input("Whoof I mean Hey my name is Noodle whats your's? ")

print("Nice to meet ya! " + name )

response = input("Would you like to play a number guessing game with me? \nyes or no? ").strip().lower()


while "yes":
    if response == "yes":
        diff = input("THAT'S GREAT! \nok ok \nWould you like to be \n1.Easy \n2.Kinda Easy \n3.Hard \n? ")
        if diff == "1":
            print("you really going to put 1 instead of typing out easy?")


    else:
        print("awwwww maybe next time.Have a good day " + name + "!")
        #OKAY i think i got it
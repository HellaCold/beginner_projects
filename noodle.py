name = input("Whoof I mean Hey my name is Noodle whats your's? ")

print("Nice to meet ya! " + name )

response = input("Would you like to play a number guessing game with me? \nyes or no? ").strip().lower()

if response == "yes":
    guess_1 = input("Awesome ill start off easy.\nI'm thinking of a number from 1-10.\What do you thin it is? ")

else:
    print("awwwww maybe next time.Have a good day " + name + "!")
        #OKAY i think i got it
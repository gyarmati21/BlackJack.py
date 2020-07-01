import random

userv = 0
pc = 0

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 1, 11]
i = 0

# the user's first two cards, userv, the dealer's first two cards, pc
while i <= 1:
    userv = userv + random.choice(cards)
    pc = pc + random.choice(cards)
    i += 1

print("Your first two cards value is: ", userv)
print("The dealer's cards value is: ", pc)

if userv == 21:
    print("Wow! A 21! EZ")
if pc == 21:
    print("Yikes! A 21 to the dealer. Better luck next time!")

while True:
    next = input("Keep your cards 'keep' or get another one 'get' : ")
    if next == "get":
        userv += random.choice(cards)
        print("Your cards value is: ", userv)
        if userv > 21:
            print("Your value is over 21, you lost.")
            break
    elif next == "keep":
        break
    else:
        print("Please either type 'get' or 'keep'")


while pc <= 18:
    if userv >= pc and userv < 22:
        pc += random.choice(cards)
        print("Dealer's value is: ", pc)
        if pc > 21:
            print("Dealer's value is over 21, you won!.")
    else:
        break

if userv <= 21 and pc <= 21:
    if userv > pc:
        print("You WON! with a score of: ", userv)
    elif userv == pc:
        print("It's a Draw! Try again.")
    else:
        print("You Lost. Better luck next time.")

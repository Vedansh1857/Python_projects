import random
def gameWin(comp , you):
    
    if comp == you:
        return None

    elif comp == 's':
        if you == 'w':
            return False

        elif you == 'g':
            return True

    elif comp == 'w':
        if you == 's':
            return True

        elif you == 'g':
            return False

    elif comp == 'g':
        if you == 's':
            return False

        elif you == 'w':
            return True

print("Computer's Turn : Snake(s), Water(w) or Gun(g) ? ")
randnum = random.randint(1, 3)

if randnum == 1:
    comp = 's'

elif randnum == 2:
    comp = 'w'

elif randnum == 3:
    comp = 'g'

you = input("Your Turn : Snake(s), Water(w) or Gun(g) ? ")

print(f"THE COMPUTER CHOSE : {comp}")
print(f"YOU CHOSE : {you}")

a = gameWin(comp, you)

if a == None:
    print("__THE GAME IS A TIE__")
elif a == True:
    print("__YOU WIN THE GAME__")
else:
    print("__YOU LOST THE GAME__")
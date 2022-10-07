import os #dingle
from os import *
def clear():
    os.system("cls")
clear()
myList = ["King", "Emperor", "Chinstrap", "Gentoo", "Little", "African", "Southern Rockhopper", "Macaroni"]
pedHab = ["", "", "", "", "", "", "", ""]
pedDiet = ["", "", "", "", "", "", "", ""]
pedAppear = ["", "", "", "", "", "", "", ""]
pedConservStat = ["", "", "", "", "", "", "", ""]
P = input ("Welcome to penguin facts. What penguin do you want to learn about?\n\n\n0. King, 1. Emperor, 2. Chinstrap, 3. Gentoo, 4. Little, 5. African, 6. Southern-Rockhopper, 7. Macaroni\n\n\n")
print("You Chose The " + myList[int(P)] + " Penguin!\n\n")
P2 = input ("What would you like to learn about the penguin?\n\n\n1. Hab, 2. Diet, 3. Appearance, 4. ConserveStatus\n\n\n")
print()
if P2 == "1":
    print(pedHab[int(P)])
elif P2 == "2":
    print(pedDiet[int(P)])
elif P2 == "3":
    print(pedAppear[int(P)])
elif P2 == "4":
    print(pedConservStat[int(P)])
else:
    print("INVAILD ANSWER")
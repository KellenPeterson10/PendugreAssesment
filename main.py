import os
from os import *
def clear():
    os.system("cls")
clear()
myList = ["King", "Emperor", "Chinstrap", "Gentoo", "Little", "African", "Southern Rockhopper", "Macaroni"]
pedHab = ["", "", "", "", "", "", "", ""]
pedDiet = ["", "", "", "", "", "", "", ""]
pedAppear = ["", "", "", "", "", "", "", ""]
pedConservStat = ["", "", "", "", "", "", "", ""]
P = input ("Welcome to penguin fact. What penguin do you want to learn about?\n\n\n0. King, 1. Emperor, 2. Chinstrap, 3. Gentoo, 4. Little, 5. African, 6. Southern-Rockhopper, 7. Macaroni\n\n\n")
print(myList[int(P)])
print(pedHab[P])









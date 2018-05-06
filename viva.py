#!/usr/bin/python

import xlrd
import sys
import os
from random import shuffle

clear = "clear"

path = sys.argv[1]
book = xlrd.open_workbook(path)
sheet = book.sheet_by_index(0)

foreign = sheet.col_values(0)
local = sheet.col_values(1)

score = 0

if len(foreign) != len(local):
    print("Something's not right in your table :/")

else:
    for i in range(0, len(foreign)):
        foreign[i] = foreign[i].lower().split("<=>")
        local[i] = local[i].lower().split("<=>")

    first = []
    second = []
    shuffled = list(range(len(foreign)))
    shuffle(shuffled)
    """"""
    print("(1) Foreign => Local")
    print("(2) Local => Foreign")

    print()
   
    option = input()

    for s in shuffled:
        if option == "1":
            first.append(foreign[s])
            second.append(local[s])
        
        else:
            first.append(local[s])
            second.append(foreign[s])

    os.system(clear)

    for i in range(0, len(first)):
        sys.stdout.write("(")
        sys.stdout.write(str(i + 1))
        sys.stdout.write(" out of ")
        sys.stdout.write(str(len(first)))
        print(")")
        sys.stdout.write("\t")
        sys.stdout.write("/".join(first[i]))
        sys.stdout.write(" => ")

        answer = input().lower()

        print()

        if answer in second[i]:
            print("Correct!")
            score += 1

        else:
            sys.stdout.write("Nah, it's ")
            sys.stdout.write(" or ".join(second[i]))
            print(".")

        input()

        os.system(clear)

    sys.stdout.write("Total score: ")
    sys.stdout.write(str(score))
    sys.stdout.write("/")
    print(str(len(first)))
    sys.stdout.write(str("{0:.2f}".format((score / len(first)) * 100)))
    print("%")

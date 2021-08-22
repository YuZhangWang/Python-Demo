def Rn(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("yes")
    else:
        print("no")

year = int(input())
Rn(year)

lis = ["John", "cena", "Randy", "orton",
       "Sheamus", "khali", "jinder mahal"]

for item in lis:
    print(item, "and", end=" ")
print()
print("--------------------------------------------")

a = ", ".join(lis)
print(a, "other wwe superstars")

a = " and ".join(lis)
print(a, "other wwe superstars")
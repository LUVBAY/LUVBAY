while True:
    n = float(input("Change owed: "))
    if n >= 0:
        break

cents = round(n * 100)
coins = 0

species = [25, 10, 5, 1]

for i in species:
    while cents >= i:
        cents -= i
        coins += 1

print(coins)

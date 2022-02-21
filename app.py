i = int(input("Please enter the number of trades: "))
a = 1
long = 0
short = 0
while a <= i:
    value = str(input(str(a) +". "))
    a = a +1
    if value.upper() == "LONG":
        long = long + 1
    elif value.upper() == "SHORT":
        short = short + 1
print("Long → " + str(long) + ", Short → " + str(short))

n1 = int(input("Positive 3-digit number: "))
n2 = 0
while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + digit

print("opposite number:", n2)
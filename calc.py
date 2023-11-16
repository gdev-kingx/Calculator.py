running = True
while running:
    print("Welcome to Calculate.AI")
    print("What Function would you Like to perform:")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exponent\n6. Modulus")
    choice = int(input("1,2,3,4,5,6: "))
    if choice == 1:
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        print(a, "+", b, "=", a + b)
    if choice == 2:
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        print(a, "-", b, "=", a - b)
    if choice == 3:
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        print(a, "*", b, "=", a * b)
    if choice == 4:
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        print(a, "/", b, "=", a / b)
    if choice == 5:
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        print(a, "^", b, "=", a ** b)
    if choice == 6:
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        print(a, "%", b, "=", a % b)

    a = input("Run Again(y/n)? ")
    if not a.lower() == "y":
        running = False
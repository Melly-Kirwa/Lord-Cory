"""Write a function named collatz() that has one parameter named number. If number is even, then
collatz should print number // 2 and return this value. if number is odd, then collatz() should
print and return 3 * number + 1."""
def collatz():
    number = input()
    try:
        if int(number) % 2 == 0:
            num = int(number) // 2
            print(f"{num}")
        else:
            num = 3 * int(number) + 1
            print(f"{num}")
        while True:
            if num == 1:
                exit()
            else:
                collatz()
    except ValueError:
        print("You must enter an integer")

collatz()
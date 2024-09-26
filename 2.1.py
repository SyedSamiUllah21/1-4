set_limit = int(input("Enter the limit: "))

for x in range(1, set_limit + 1):
    
    if x % 3 == 0 and x % 5 == 0:
        print("fizz buzz")
    elif x % 3 == 0:
        print("izz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)

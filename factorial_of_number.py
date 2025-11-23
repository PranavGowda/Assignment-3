def fact(num):
    if num == 1:
        return 1
    else:
        factrial= num * fact(num-1)
        return factrial
n=int(input("enter the number "))
print(f"The factorial of {n} using recursion is {fact(n)}")



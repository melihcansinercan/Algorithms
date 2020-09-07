n=int(input("How many elements do you want to see for fibonacci"))
def fibonacci(n):
    if n<2:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))
for n in range(0,n):
    print('fib',n,':',fibonacci(n))



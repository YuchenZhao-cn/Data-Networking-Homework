def JudgePrime(num):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               print(num, " is not a prime number")
               break
       else:
           print(num, "is a prime number")
    else:
       print(num, " is not a prime number")

while True:
    num = int(input("Type in a number, type in \"-1\" to quit: "))
    if num == -1:
        break
    else:
        JudgePrime(num)
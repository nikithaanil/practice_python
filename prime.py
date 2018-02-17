'''  Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).'''

def checkPrime(num):
    prime = 1

    for i in range(2,num):
        if num % i == 0:
            prime = 0
    return prime



def main():
    n = int(input("enter the number to check for primality: "))

    if n == 1:
        print("{} is neither prime nor composite".format(n))
    elif n == 2:
        print("{} is a prime number".format(n))
    else:
        result = checkPrime(n)
        if result == 1:
            print ("the number is prime ")
        else:
            print ("the number is not prime ")



if __name__ == "__main__":
    main()

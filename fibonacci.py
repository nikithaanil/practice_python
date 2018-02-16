''' Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)'''


fib=[]
def fibonacci(a,b,limit):
    while limit > 0 :
        sum = a + b
        fib.append(sum)
        a = b
        b = sum
        limit =limit - 1
    print(fib)

def main():
    a = 1
    b = 2
    count = int(input("\nenter the limit: "))
    if count == 2:
        fib.append(a)
        fib.append(b)
        print(fib)
    elif count >= 3:
        fib.append(a)
        fib.append(b)
        count=count-2
        fibonacci(a,b,count)


if __name__ == "__main__":
    main()

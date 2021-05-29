def generateFibonacci(n):
    seq = [1,1]
    [seq.append(seq[-1] + seq[-2]) for x in range(n)]
    return seq[0:n]

num = input("How many Fibonacci numbers to generate: ")
fib_seq = generateFibonacci(int(num))
print("Fibonacci sequence generated: ",fib_seq)

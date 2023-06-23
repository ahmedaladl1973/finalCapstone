# 

def find_missing_fibonacci_number(n):
  
  # Initialize the first two terms of the sequence.
  a, b = 0, 1

  # Calculate the first n Fibonacci numbers.
  for i in range(n + 1):
    a, b = b, a + b

  # Find the missing Fibonacci number.
  for i in range(n + 1):
    if a == n:
      return b
    a, b = b, a + b


num=find_missing_fibonacci_number(5)
print(num)

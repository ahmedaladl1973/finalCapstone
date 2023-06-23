# Arithmetic sequence calculator
# By: Ahmed AlAdl
# Version 1.0


def nth_term_arithmetic_sequence(sequence, n):
 
  #if n < 0 or n >= len(sequence):
   # raise ValueError("Invalid n")

  # Calculate the common difference between the terms of the sequence.
  d = sequence[1] - sequence[0]

  # Calculate the nth term of the sequence.
  return sequence[0] + d * (n - 1)

num=nth_term_arithmetic_sequence([5,10,15,20], 10)
print(num)
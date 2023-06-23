# Solve sequences
# by: Ahmed AlAdl
# Version 1.0.0



def find_sequence_type(sequence):
 # Find the sequence type. 
 # By Ahmed AlAdl
 # Version 1.0.0 
    # Check if the sequence is empty.
    if not sequence:
     raise ValueError("The sequence cannot be empty.")

    # Check if the sequence is Fibonacci.
    def fibonacci_sequence(fib_sequence):

    #  Check if the rest of the terms are the sum of the two preceding terms.

        for i in range(2, len(fib_sequence)):
         if fib_sequence[i] != fib_sequence[i - 1] + fib_sequence[i - 2]:
          return False

        return True
 
    fib=fibonacci_sequence(sequence)
    if fib == True:
     return "Fibonacci"

   # Check if the sequence is constant.
    common_difference = sequence[1] - sequence[0]
    if common_difference == 0:
     return "Constant"
     
    # Check if the sequence is arithmetic.

    common_difference = sequence[1] - sequence[0]
    for i in range(1, len(sequence) - 1):
        if sequence[i + 1] - sequence[i] != common_difference:
         common_difference = None
        break

    if common_difference is not None:
        return "Arithmetic"

    # Check if the sequence is geometric.

    common_ratio = sequence[1] / sequence[0]
    for i in range(1, len(sequence) - 1):
        if sequence[i + 1] / sequence[i] != common_ratio:
         common_ratio = None
        break

    if common_ratio is not None:
     return "Geometric"
     
  
def nth_term_arithmetic_sequence(sequence, n):
 # Arithmetic sequence calculator
 # By: Ahmed AlAdl
 # Version 1.0
 
 # Calculate the common difference between the terms of the sequence.
  d = sequence[1] - sequence[0]

  # Calculate the nth term of the sequence.
  return sequence[0] + d * (n - 1)

def nth_term_geometric_sequence(sequence, n):
 # Geometric sequence calculator
 # By: Ahmed AlAdl
 # Version 1.0

  # Calculate the common ratio between the terms of the sequence.
  r = sequence[1] / sequence[0]

  # Calculate the nth term of the sequence.
  return sequence[0] * r ** (n - 1)

#Input sequence.
seq = input("Enter a list of integers: ").split()

# Convert the sequence to a list of integers.
seq = [int(i) for i in seq]

# Input the nth term.
n = int(input("Enter the nth term: "))

# Find the sequence type.
seq_type=find_sequence_type(sequence=seq)

# Find nth term.
if seq_type == "Arithmetic":
 output=nth_term_arithmetic_sequence(sequence=seq, n=n)

elif seq_type == "Geometric":
 output=nth_term_geometric_sequence(sequence=seq, n=n)    

# Print the sequence type.
print("The sequence is: " +str(seq))
print("Sequence type: " + seq_type)
print("The " + str(n)+"th term is: " + str(output))



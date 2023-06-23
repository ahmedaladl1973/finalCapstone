# Find the sequence type. By Ahmed AlAdl
# Version 1.0.0

def find_sequence_type(sequence):
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
   

#Input sequence.
seq = input("Enter a list of integers: ").split()

# Convert the sequence to a list of integers.
seq = [int(i) for i in seq]

# Find the sequence type.
output=find_sequence_type(sequence=seq)

# Print the sequence type.
print(output)



# End of code


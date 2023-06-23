# Liner Sequence Calculator
# By Ahmed AlAdl
# Version 1.0

# Find Common Differnce 
def find_common_difference(sequence):

  if len(sequence) < 2:
    raise ValueError("Sequence must have at least two terms.")

  # Calculate the difference between the first two terms.
  common_difference = sequence[1] - sequence[0]

  # Check if the difference is the same for all of the terms in the sequence.
  for i in range(2, len(sequence)):
    if sequence[i] - sequence[i - 1] != common_difference:
      raise ValueError("The sequence does not have a common difference.")

  return common_difference

# Solce Linear Sequence
def solve_linear_sequence(first_term, common_difference, n):
  if n < 0:
    raise ValueError("Invalid n")

  return first_term + common_difference * (n - 1)


#Input sequence.
seq = input("Enter a list of integers: ").split()

# Convert the sequence to a list of integers.
seq = [int(i) for i in seq]

# Input the nth term.
n = int(input("Enter the nth term: "))

# Find Common Difernce
dif=find_common_difference(seq)

# Solve Liner Sequence
output=solve_linear_sequence(seq[0], dif, n)

# Print the sequence type.
print("The sequence is: " +str(seq))
print("The difference is: " +str(dif))
print("The " + str(n)+"th term is: " + str(output))

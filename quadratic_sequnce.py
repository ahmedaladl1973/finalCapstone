# Identifi and solve linear and quadratic sequnces
# By Ahmed AlAdl


def is_linear(seq):
  """Returns True if the sequence is linear, False otherwise."""
  for i in range(1, len(seq)):
    if seq[i] - seq[i - 1] != seq[1] - seq[0]:
      return False
  return True
'''
def is_quadratic(seq):
  """Returns True if the sequence is quadratic, False otherwise."""
  for i in range(2, len(seq)):
    if (seq[i] - seq[i - 1]) - (seq[i - 1] - seq[i - 2]) != seq[1] - seq[0]:
      return False
  return True
'''

def is_quadratic(seq):
   # Check if the sequence has at least 3 terms.
  if len(seq) < 3:
    return False

  # Calculate the second difference between successive terms.
  second_difference = []
  for i in range(2, len(seq)):
    second_difference.append(seq[i] - 2 * seq[i - 1] + seq[i - 2])

  # Check if the second difference is constant.
  return len(set(second_difference)) == 1

def solve_nth_number(seq, n):
  """Returns the nth number in the sequence."""
  if is_linear(seq):
    return seq[0] + (n - 1) * (seq[1] - seq[0])
  elif is_quadratic(seq):
    a = (seq[2] - 2 * seq[1] + seq[0]) / 2
    b = (seq[1] - seq[0] - 3 * a)
    c = seq[0] - a - b
    return a * n**2 + b * n + c
  else:
    raise ValueError("The sequence is not linear or quadratic.")

#Input sequence.
seq = input("Enter a list of integers: ").split()

# Convert the sequence to a list of integers.
seq = [int(i) for i in seq]

# Input the nth number of sequences
nth = int(input("Input the nth number of sequences :"))

if is_linear(seq):
  print("The sequence is linear.")
  nth_number = solve_nth_number(seq, nth)
  print("The " + str(nth) + " number in the sequence is: ", nth_number)
elif is_quadratic(seq):
  print("The sequence is quadratic.")
  nth_number = solve_nth_number(seq, nth)
  print("The " + str(nth) + " number in the sequence is: ", nth_number)
else:
  print("The sequence is not linear or quadratic.")  
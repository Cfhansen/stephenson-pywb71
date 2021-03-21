###solution to exercise 71 from ben stephenson's "the python workbook".

error = 1.0 * 10 ** (-12)

num_for_sqrt = float(input('Enter a number:'))

guess = num_for_sqrt / 2
trials = 0

while abs(guess ** 2 - num_for_sqrt) > error and trials < 10000:
  trials += 1
  guess = (guess + (num_for_sqrt / guess)) / 2

print(guess)

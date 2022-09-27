import sys

firstNum = int(sys.argv[1])
lastNum = int(sys.argv[2])

for i in range(firstNum, lastNum + 1):
  if i > 1:
    for j in range(2, i + 1):
      if (i % j == 0):
        break
      else:
        print(f"Prime Number between {firstNum} and {lastNum} are: {i}")
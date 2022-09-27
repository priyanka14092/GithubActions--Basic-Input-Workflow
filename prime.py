import sys

firstNum = int(sys.argv[1])
lastNum = int(sys.argv[2])

print(f"Prime Number between {firstNum} and {lastNum} are: ", end = ' ')
for i in range(firstNum, lastNum + 1):
  count = 0
  for j in range(2, i // 2 + 1):
    if (i % j == 0):
      count = count + 1
      break
  if (count == 0 and i != 1):
    print(f"{i} ", end = ' ')
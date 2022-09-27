# import os

firstNum = os.environ['firstNum']
lastNum = os.environ['secondNum']

for i in range(firstNum, lastNum + 1):
  if i > 1:
    for j in range(2, i + 1):
      if (i % j == 0):
        break
      else:
        print(f"Prime Number between {firstNum} and {lastNum} are: {i}")

# run: |
#       echo "Store: ${{ github.event.inputs.myInput }}"
#       INPUT_STORE=${{ github.event.inputs.myInput }} python3 test.py
# test.py file:

# import os

# input_variable = os.environ['INPUT_STORE']

# print("Input Variable:", input_variable)
"""Median calculator."""
"""Salihah Alnahdi K20055346"""

from tokenize import Double

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        if len(numbers) % 2 ==0:
            firstNumber = numbers[int(len(numbers)/2)]
            secondNumber = numbers[int((len(numbers)/2)-1)]
            median = (int(firstNumber+secondNumber))/2
            print(median)
        elif len(numbers) % 2 !=0:
              median = numbers[int((len(numbers)-1)/2)]
              print(median)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break


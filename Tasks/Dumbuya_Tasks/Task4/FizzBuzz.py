def FizzBuzz(numbers):
    for i, item in enumerate(numbers):
        if item % 3 == 0 and item % 5 == 0:
            numbers[i] = 'FizzBuzz'
        elif item % 5 == 0:
            numbers[i] = 'Buzz'
        elif item % 3 == 0:
            numbers[i] = 'Fizz'

    return numbers


List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
print(FizzBuzz(List))

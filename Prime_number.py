number = int(input('please enter your number: '))
accumulator = 0
for i in range(1, number+1):
    if number % i == 0:
        accumulator += 1
if accumulator == 2:
    print('your number is prime')
else:
    print('your number is not prime')
